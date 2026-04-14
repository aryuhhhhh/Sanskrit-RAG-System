def get_retriever(vector_store, k=5):
    """
    Returns a retriever object from the vector store to fetch the
    top k most similar text chunks based on the user's query.
    k increased to 5 for better context inclusion.
    """
    return vector_store.as_retriever(search_kwargs={"k": k})
