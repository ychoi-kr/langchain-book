from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda

load_dotenv()


prompt = PromptTemplate.from_template(
    """요리 레시피를 생각해 보세요.

요리 이름: {dish}"""
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

output_parser = StrOutputParser()


def upper(inp: str) -> str:
    return inp.upper()


chain = prompt | model | output_parser | RunnableLambda(upper)


result = chain.invoke({"dish": "카레"})
print(type(result))
print(result)
