from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

load_dotenv()

set_debug(True)

cot_prompt = PromptTemplate.from_template(
    """다음 질문에 답하세요.

{question}
                                       
단계별로 생각해 봅시다."""
)

summarize_prompt = PromptTemplate.from_template(
    """다음 문장을 결론만 간단히 요약하세요.

{text}"""
)
model = ChatOpenAI(model="gpt-3.5-turbo")

chain1 = {"question": RunnablePassthrough()} | cot_prompt | model | StrOutputParser()
chain2 = {"text": RunnablePassthrough()} | summarize_prompt | model | StrOutputParser()

chain = chain1 | chain2

result = chain.invoke("3*3+4*4")
print(result)
