import streamlit as st
from utils import load_pdf, build_vectorstore
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

st.set_page_config(page_title="RAG Demo", page_icon="✨")

st.title("RAG Demo App")
st.write("Upload a PDF, then ask questions about it!")

GROQ_API_KEY = ""  


uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    docs = load_pdf(uploaded_file)
    vectordb = build_vectorstore(docs)

    retriever = vectordb.as_retriever()

    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    query = st.text_input("Ask a question about the document:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa.run(query)
        st.write("### 📌 Answer:")
        st.write(answer)
