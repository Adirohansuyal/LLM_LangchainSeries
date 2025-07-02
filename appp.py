# ==========================================
# 🔐 Private LLM Q&A App (Admin + User Setup)
# ==========================================
# This is the complete setup:
# - Admin script to prepare embeddings
# - Streamlit frontend app (no upload)
# - Powered by LangChain + FAISS + Gemma-2B API

### 🔧 ADMIN SCRIPT: Run once to prepare vectorstore

# admin_vectorize.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
import pickle
import os

# ✅ 1. Add your backend PDFs here
pdf_paths = [
    "docs/Profile-2.pdf",
    "docs/www-birlainstitute-co-in-....pdf",
    "docs/Aditya_Suyal_Resume.pdf"
]

all_docs = []

# ✅ 2. Load, split, and embed content
for path in pdf_paths:
    loader = PyPDFLoader(path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    all_docs.extend(splitter.split_documents(pages))

# ✅ 3. Generate embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(all_docs, embeddings)

# ✅ 4. Save vectorstore index
with open("vectorstore_index.pkl", "wb") as f:
    pickle.dump(vectorstore, f)

print("✅ Vectorstore saved to vectorstore_index.pkl")


### 🧑‍💻 FRONTEND APP (Streamlit UI for end users)

# app.py

import streamlit as st
from huggingface_hub import InferenceClient
import pickle

# Title
st.set_page_config(page_title="RAG Based Streamlit Private Q&A App with LangChain and FAISS")
st.title("🤖 RAG Based Streamlit Private Q&A App with LangChain and FAISS")

# Hugging Face API token
import os


# ✅ Securely fetch the Hugging Face token
HUGGINGFACE_TOKEN = st.secrets["HUGGINGFACE_TOKEN"]

# Set Streamlit app title
st.set_page_config(page_title="RAG Based Streamlit Private Q&A App with LangChain and FAISS")
st.title("🤖 RAG Based Streamlit Private Q&A App with LangChain and FAISS")



# Load Gemma client
@st.cache_resource
def load_llm():
    return InferenceClient(model="google/gemma-2b-it", token=HUGGINGFACE_TOKEN)

llm = load_llm()

# Load FAISS index
@st.cache_resource
def load_vectorstore():
    with open("vectorstore_index.pkl", "rb") as f:
        return pickle.load(f)

vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever()

# Ask a question
question = st.text_input("Ask your question about the documents")

# Generate answer
if question:
    with st.spinner("Thinking..."):
        docs = retriever.get_relevant_documents(question)
        context = "\n".join([doc.page_content for doc in docs[:3]])

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.You have to carefully search for user question's answer in your knowledge. Answer the user's question using ONLY the information provided in the context. Respond naturally and directly, as if you are sharing your knowledge, without explicitly referencing the text or context. Please ignore the Case of the questions asked by the user."
            },
            {
                "role": "user",
                "content": f"Context: {context}\nQuestion: {question}"
            }
        ]

        response = llm.chat_completion(messages=messages)
        answer = response.choices[0].message["content"]

        st.success(answer)

        with st.expander("View Source Context"):
            for i, doc in enumerate(docs[:3]):
                st.markdown(f"**Chunk {i+1}:**")
                st.code(doc.page_content[:700])



