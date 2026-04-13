from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedder(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Initializes and returns the HuggingFace embedding model specifically
    configured to run efficiently on the CPU.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return embeddings
