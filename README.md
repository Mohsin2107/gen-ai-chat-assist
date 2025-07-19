# 📄 GenAI Chat Assist

> A local document-based chatbot powered by Mistral 7B using LangChain + Ollama. Ask questions from your PDF or TXT files, entirely offline.

![Streamlit UI](https://img.shields.io/badge/Built%20With-Streamlit-orange?style=flat-square)
![Ollama LLM](https://img.shields.io/badge/Model-Mistral_7B-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/RAG-LangChain-green?style=flat-square)
![Status](https://img.shields.io/badge/API-Free_%26_Offline-lightgrey?style=flat-square)

---

## 🚀 Features

- 📥 Upload `.pdf` or `.txt` knowledge files
- 🤖 Chat with the content in natural language
- 🧠 Uses **LangChain RAG pipeline** for retrieval
- ⚙️ Powered by **Mistral LLM** via **Ollama**
- ✅ Fully offline (no API key required)

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Serving:** Ollama (`mistral`)  
- **RAG Pipeline:** LangChain  
- **Embeddings & Vector Store:** ChromaDB  
- **PDF Reader:** PyMuPDF (fitz)  

---

## 📦 Installation

```bash
git clone https://github.com/mohsin2107/genai-chat-assist.git
cd genai-chat-assist
pip install -r requirements.txt
