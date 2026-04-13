import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_documents(data_dir: str):
    """
    Loads text and PDF documents from the specified directory.
    Returns a list of LangChain Document objects.
    """
    documents = []
    
    if not os.path.exists(data_dir):
        print(f"Warning: Directory '{data_dir}' does not exist.")
        return documents

    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if filename.endswith(".txt"):
            try:
                loader = TextLoader(filepath, encoding='utf-8')
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {filename}: {e}")
                
        elif filename.endswith(".pdf"):
            try:
                loader = PyPDFLoader(filepath)
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {filename}: {e}")
                
    return documents
