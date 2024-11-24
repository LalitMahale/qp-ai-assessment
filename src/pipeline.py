from src.document_process import Document_loader
from src.chunking import Chunking
from src.db import Vectordb
import os
import streamlit as st

def rag_pipeline(filepath:str,db_path:str):
    try:
        doc = Document_loader(doc_path=filepath).data_extractor()
        st.sidebar.info("Stpe 1: Data Loaded.")
        chunk = Chunking().split_chunk(doc=doc)
        st.sidebar.info("Stpe 2: Chunk created.")
        Vectordb().store_vectors(chunks=chunk,db_name=db_path)
        st.sidebar.info("Stpe 3: Vector created and stored in DB ")
        return True
    except Exception as e:
        return f"There is some error {e}"

def qa_pipeline(query:str,db_path:str):
    retriever = Vectordb().vector_retriever(query=query,db_path=db_path)
    text = Chunking(chunk_overlap=50,chunk_size=500).chunk_merge(chunks=retriever)
    return text