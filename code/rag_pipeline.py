from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def build_rag_pipeline(llm, retriever):
    """
    Constructs the end-to-end RAG pipeline isolating retrieval and generation.
    Uses strict prompt engineering to completely halt hallucination and enforce Sanskrit extraction.
    """
    template = """You are a highly structured Sanskrit question answering system.

STRICT RULES:
1. Answer ONLY using the information provided in the Context.
2. Under NO circumstances should you use your outside knowledge or hallucinate.
3. Your answer MUST be a COMPLETE Sanskrit sentence. Do NOT return one-word answers.
4. If the answer to the Question is not present in the Context, you MUST reply exactly with: 'दत्ते सन्दर्भे उत्तरं नास्ति'
5. Your required output language is STRICTLY Sanskrit.

Context:
{context}

Question: {question}

Answer strictly in a COMPLETE Sanskrit sentence:"""
    
    prompt = PromptTemplate.from_template(template)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt, "document_separator": "\n\n"}
    )
    
    return qa_chain