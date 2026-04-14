from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents, chunk_size=350, chunk_overlap=30):
    """
    Splits documents into smaller chunks for embedding and retrieval.
    chunk_size reduced to prevent memory crashes on 8GB CPU environments.
    Includes the Sanskrit poorna virama (।) as a sentence separator.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "॥", "।", " ", ""] 
    )
    
    chunks = text_splitter.split_documents(documents)
    
    # Context Cleaning: Remove very short, disconnected noisy chunks
    clean_chunks = [chunk for chunk in chunks if len(chunk.page_content.strip()) > 20]
    return clean_chunks
