# 📄 AskMyDocs – GenAI Document Question Answering System

AskMyDocs is a **Retrieval-Augmented Generation (RAG)** based application that allows users to **upload documents and ask questions** using Large Language Models.  
The system retrieves relevant context from documents using a **vector database** and generates accurate, context-aware answers.

This project demonstrates **real-world GenAI architecture** with a clear separation of API, service, vector storage, and UI layers.

---

## 🚀 Features
- Upload and process documents
- Semantic search using vector embeddings
- Context-aware question answering (RAG)
- FastAPI-based backend
- Interactive Streamlit UI
- Modular and scalable architecture

---

## 🧠 Tech Stack
- **Python**
- **FastAPI**
- **LangChain**
- **ChromaDB (Vector Store)**
- **Streamlit**
- **LLMs / Embeddings**
- **Git & GitHub**

---

## 📂 Project Architecture

```
AskMyDocs/
├── app/
│ ├── api/ # FastAPI routes (document upload & query)
│ ├── services/ # RAG logic, embeddings, LLM calls
│ └── Main.py # Backend entry point
│
├── UI/
│ └── streamlit_app.py # Streamlit frontend
│
├── vector_store/
│ ├── chroma/ # ChromaDB persistence
│ └── db.py # Vector store configuration
├── requirements.txt
├── README.md

```
