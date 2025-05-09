import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_core._api.deprecation import LangChainDeprecationWarning
import warnings

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

load_dotenv()

@st.cache_resource
def setup_chain():
    loader = TextLoader("smart_homes_info.txt", encoding='utf-8')
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding, persist_directory="chroma_index")
    vectorstore.persist()

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

    return qa_chain

st.set_page_config(page_title="EcoNest Chatbot", layout="centered")
st.title("EcoNest Smart Home Assistant")
st.caption("Ask any question about EcoNest's smart home products.")

qa_chain = setup_chain()

query = st.text_input("💬 Your Question:")
if query:
    with st.spinner("Thinking..."):
        response = qa_chain.invoke({"query": query})
        st.success(response["result"])
