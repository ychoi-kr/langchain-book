import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

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
        response = "안녕하세요"
        history.add_ai_message(response)
        st.markdown(response)

