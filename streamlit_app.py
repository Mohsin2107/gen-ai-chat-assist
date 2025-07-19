import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from utils.retriever import build_retriever
from utils.pdf_reader import extract_text_from_pdf
import os

st.set_page_config(page_title="GenAI Chat Assist (Ollama)", layout="wide")
st.title("💬 GenAI Chat Assist with Local LLM (Mistral)")

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()
    if file_type == "txt":
        raw_text = uploaded_file.read().decode("utf-8")
    elif file_type == "pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        st.error("Unsupported file type")
        st.stop()

    with open("knowledge.txt", "w") as f:
        f.write(raw_text)

    st.success("Knowledge base uploaded!")
    retriever = build_retriever("knowledge.txt")
    llm = Ollama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    user_question = st.text_input("Ask a question:")
    if user_question:
        st.session_state.messages.append(("user", user_question))
        answer = qa_chain.run(user_question)
        st.session_state.messages.append(("assistant", answer))

for role, msg in st.session_state.messages:
    label = "🧑 You:" if role == "user" else "🤖 Mistral:"
    st.markdown(f"**{label}** {msg}")
