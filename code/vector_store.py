import os
from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, embedder, save_path="faiss_index"):
    """
    Builds a FAISS vector store from document chunks and saves it locally.
    """
    vector_store = FAISS.from_documents(chunks, embedder)
    vector_store.save_local(save_path)
    return vector_store

def load_vector_store(embedder, load_path="faiss_index"):
    """
    Loads a locally saved FAISS vector store.
    """
    if os.path.exists(load_path) and os.path.exists(os.path.join(load_path, "index.faiss")):
        return FAISS.load_local(
            load_path, 
            embedder, 
            allow_dangerous_deserialization=True # required for local faiss loading as of recent updates
        )
    return None
