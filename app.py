import streamlit as st
from src.chatbot import chat


st.set_page_config(
    page_title="Magic Juice Assistant",
    page_icon="🧃",
    layout="centered"
)


st.title("🧃 Magic Juice Assistant")
st.write("Ask me anything about Magic Juice.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask a question about Magic Juice..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(prompt)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
