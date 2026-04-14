from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

def get_llm(model_id="google/flan-t5-small"):
    """
    Initializes a highly lightweight and simplistic CPU-friendly LLM.
    Flan-T5-small ensures maximum speed on lower-end devices while maintaining accuracy.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id, 
        low_cpu_mem_usage=True
    )
    
    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=50,
        do_sample=False,
        device=-1 # Forcing CPU
    )
    
    return HuggingFacePipeline(pipeline=pipe)