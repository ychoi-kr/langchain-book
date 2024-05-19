from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()


prompt = PromptTemplate.from_template(
    """요리 레시피를 생각해줘.

요리 이름: {dish}"""
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = prompt | model

result = chain.invoke({"dish": "카레"})
print(result.content)
