## RAG DEMO PROJECT

This is a **Retrieval-Augmented Generation (RAG)** demo project where users can easily upload any document or data source of their choice and get **accurate, context-aware answers** based on that content.

---

##  Overview

This project demonstrates a simple yet powerful **RAG pipeline** using the following tech stack:

- **Frontend:** [Streamlit](https://streamlit.io) — for an interactive and minimal UI.  
- **LLM:** [Groq API](https://groq.com) — used for generating high-quality, low-latency responses.  
- **Vector Database:** [Chroma DB](https://www.trychroma.com) — to efficiently store and retrieve document embeddings.  
- **Embedding Model:** [`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — from Hugging Face, used to generate semantic vector representations of the uploaded documents.  

---

##  Features

- 📂 Upload files (PDFs, text, etc.) as a custom knowledge base.  
- 🔍 Ask natural language questions and get precise answers grounded in your data.  
- ⚡ Fast inference using **Groq’s LLM API**.  
- 🧩 Modular, easy-to-extend RAG architecture.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| Vector DB | Chroma |
| Embeddings | Hugging Face Sentence Transformer |
| LLM | Groq API |
| Environment | `.env` for secure key storage |

---


