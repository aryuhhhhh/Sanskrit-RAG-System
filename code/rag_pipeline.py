from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def build_rag_pipeline(llm, retriever):
    """
    Constructs the end-to-end RAG pipeline isolating retrieval and generation.
    Uses strict prompt engineering to completely halt hallucination and enforce Sanskrit extraction.
    """
    template = """You are a Sanskrit question answering system.

Answer ONLY using the given context.
Do NOT generate unrelated text.
If answer is not found, say: 'उत्तर उपलब्ध नहीं है'.

Context:
{context}

Question: {question}

Answer in Sanskrit:"""
    
    prompt = PromptTemplate.from_template(template)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt, "document_separator": "\n\n"}
    )
    
    return qa_chain