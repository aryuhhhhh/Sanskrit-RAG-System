# Sanskrit Document RAG System: Technical Report

## 1. Introduction
This report outlines the technical blueprint, algorithmic selection, and specific design methodologies chosen to construct a pure CPU-oriented Retrieval-Augmented Architecture tailored for digesting unstructured Indology and Sanskrit textual data. RAG eliminates hallucination inherent to purely generative networks by firmly appending source context constraints. 

## 2. System Architecture
The pipeline establishes stringent separation of concerns ensuring component modularity:
- **DataLoader Layer**: Parses standard text documents alongside raw PDF extractions leveraging pure Python bridges (`PyPDFLoader`).
- **Semantic Chunking**: Employs LangChain's Recursive Splitting, augmented to slice contextual trees optimally for the 500-token barrier constraints of standard attention windows.
- **Embedding/Vector Layer**: CPU-bound translation mechanism mapping lexical syntax semantics to geometry arrays.
- **Generative QA Synthesis**: Instruct-tuned LLM execution evaluating solely mathematical nearest neighbor vectors returned precisely by FAISS engines.

## 3. Data Processing (Sanskrit-specific handling)
A foundational challenge targeting Sanskrit texts concerns the absence of typical western syntactic breaks. In the `chunker.py`, the boundary split arrays (`separators`) logically prepend standard `\n` carriage returns with the *poorna virama* character (the visual vertical bar `।`). This ensures paragraphs and *slokas* aren't truncated directly across an active thought line before chunking enforces the 500 character limitation barrier.

## 4. Embedding Strategy
To maintain processing efficiency across strict CPU-only constraints, the model leverages `sentence-transformers/all-MiniLM-L6-v2`. 
- **Efficiency:** Produces mathematically sparse 384-dimensional embeddings, resulting directly in micro-second fast retrieval traversals compared to dense 1024 arrays found in heavier transformers (e.g., standard Bert).
- **Scale:** Footprint guarantees no thermal or memory bottlenecking inside single-threaded instances.

## 5. Retrieval Method
**FAISS** (Facebook AI Similarity Search) drives local retrieval storage. It compiles C++ optimized arrays specifically handling high-volume flat vector evaluations (L2 Norm or Inner Product matrices) incredibly efficiently across CPU matrices. Search parameter extraction leverages `k=3` bounds (returning top 3 paragraphs) mitigating input context saturation to the underlying sequence model.

## 6. LLM Selection (CPU reasoning)
Generation heavily isolates `google/flan-t5-small`.
- T5 parameters execute on traditional consumer architectures cleanly against isolated memory caches without needing specialized quantized GGUF/llama.cpp binary compiling.
- Why Flan? FLAN enforces strictly 'Instruction Finetuning'. As opposed to `distilgpt2` which attempts to autocompelte text blocks broadly, FLAN natively understands directive prompts (e.g., "Use the following context to answer..."). This makes extracting accurate results substantially cleaner on low-resource architectures.

## 7. Performance Considerations
The system's entire memory overhead is carefully calibrated to demand less than 2 Gigabytes of RAM actively traversing its `RetrievalQA` pipeline. Embedding happens seamlessly as FAISS index caches on generic NVMe/SSD IO storage enabling almost instant downstream boot cycles during `mode query` operations.

## 8. Limitations
- **Linguistics:** The foundation models (`all-MiniLM-L6-v2`, `flan-t5`) possess limited deep native representation for raw Devanagari script syntax. Queries generated via Latin transliteration (ITRANS/Harvard-Kyoto) typically extract more robust proximity matching against English commentaries mixed with Sanskrit roots.
- **Generation Capacity:** `flan-t5-small` strictly summarizes QA blocks succinctly. It will not generate elaborate synthesized multi-page outputs comparable to parameters reaching the multi-billion parameter echelons.

## 9. Future Improvements
Targeting deeper native language evaluation naturally necessitates indexing an Indic-specific transformer mapping sequence (e.g., AI4Bharat `Indic-BERT`) paired natively with compiled quantized binaries (e.g., unsloth or llama.cpp driving specifically an 8-bit `Llama-3-8b` execution core) to support heavy native output generation while respecting absolute CPU-only infrastructure limitations.
