from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="steps to make the dish")


output_parser = PydanticOutputParser(pydantic_object=Recipe)

prompt = PromptTemplate.from_template(
    """요리 레시피를 생각해줘.

{format_instructions}

요리 이름: {dish}""",
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

model = ChatOpenAI(model="gpt-3.5-turbo").bind(
    response_format={"type": "json_object"}
)

chain = prompt | model | output_parser

result = chain.invoke({"dish": "카레"})
print(type(result))
print(result)
