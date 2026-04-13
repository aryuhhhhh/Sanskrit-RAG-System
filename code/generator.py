from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

def get_llm(model_id="google/flan-t5-base"):
    """
    Initializes an upgraded CPU-friendly LLM for answer generation.
    Flan-T5-base improves translation/extraction fidelity while keeping limits.
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
        max_new_tokens=100,
        do_sample=False, # Lowers memory footprint, disables beam search
        device=-1 # CPU Mode explicitly enforced
    )
    
    return HuggingFacePipeline(pipeline=pipe)