import streamlit as st

st.title("simple chatbot")

question=st.text_input("ask me everything")

if st.button("send"):
    st.write("you asked ", question)
    st.write("chatbot is on the process pf answering your question")