import os

import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

st.title("langchain-streamlit-app")

history = StreamlitChatMessageHistory()

for message in history.messages:
    st.chat_message(message.type).write(message.content)

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        history.add_user_message(prompt)
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = ChatOpenAI(
            model_name=os.environ["OPENAI_API_MODEL"],
            temperature=os.environ["OPENAI_API_TEMPERATURE"],
        )
        messages = [HumanMessage(content=prompt)]
        response = chat.invoke(messages)
        history.add_ai_message(response)
        st.markdown(response.content)
