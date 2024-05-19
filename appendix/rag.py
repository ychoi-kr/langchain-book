from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores.faiss import FAISS

load_dotenv()

texts = [
    "저의 취미는 독서입니다.",
    "제가 좋아하는 음식은 카레입니다.",
    "제가 싫어하는 음식은 만두입니다.",
]
vectorstore = FAISS.from_texts(texts, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

prompt = ChatPromptTemplate.from_template(
    """다음 context에만 기반해 답변해 주세요.

{context}

질문: {question}
"""
)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

output_parser = StrOutputParser()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | output_parser
)

result = chain.invoke("제가 좋아하는 음식은 무엇일까요?")
print(result)
