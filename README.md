# Sanskrit Document Retrieval-Augmented Generation (RAG) System

A modular, clean, and entirely CPU-efficient Retrieval-Augmented Generation (RAG) framework optimized for small-scale Sanskrit and Indology documents. Built on LangChain framework ensuring well-separated retrieval and generation paths.

## Project Overview

This architecture builds an information retrieval system that operates seamlessly on local non-GPU consumer hardware while preventing LLM hallucination by rooting answers firmly in indexed source texts.

## Architecture Explanation

1. **Loader (`loader.py`)**: Responsible for mapping unstructured raw files (`.txt`, `.pdf`) from the `data/` directory to structured LangChain Documents.
2. **Chunker (`chunker.py`)**: Splits massive texts into coherent paragraphs (chunk_size=500). Modifies standard splitting algorithms to additionally recognize the Sanskrit *poorna virama* (`।`) for safer boundary separation.
3. **Embedder (`embedder.py`)**: Converts semantic meanings into mathematically dense vectors using a lightweight but efficient HuggingFace Sentence Transformer (`all-MiniLM-L6-v2`) limited explicitly to the CPU.
4. **Vector Store (`vector_store.py`)**: Uses Facebook AI Similarity Search (FAISS) local indices to store document embeddings mapped against their source text geometries.
5. **Retriever (`retriever.py`)**: Performs scalable vector-proximity searches fetching the semantic top 3 highly relevant paragraphs from the FAISS local database.
6. **Generator (`generator.py`)**: Evaluates retrieved chunks alongside user questions using an instruction-tuned language model `google/flan-t5-small`.
7. **RAG Pipeline (`rag_pipeline.py`)**: Chain abstraction to bind retrieval output seamlessly to the generation step.

## Tech Stack

* **Python 3.10 / 3.11**
* **LangChain**: High-level abstract coordination layer.
* **FAISS**: In-memory dense similarity CPU-specific retrieval.
* **sentence-transformers**: Context embedding (`all-MiniLM-L6-v2`).
* **HuggingFace Transformers**: Extractive QA and Generation (`google/flan-t5-small`).
* **PyPDF**: Local processing for Sanskrit texts stored in pdf wrappers.

## Setup Instructions

### Environment Activation
Create and activate an isolated python environment:
```bash
python -m venv venv
# On Windows
venv\\Scripts\\activate
# On Linux/MacOS
source venv/bin/activate
```

### Installation
Ensure that you are running Python 3.10 or 3.11. Install CPU specific libraries defined in the `requirements.txt`:
```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Ingest Data
Put your `.pdf` or `.txt` Sanskrit literature into the auto-generated `data/` folder and trigger ingestion:
```bash
python code/main.py --mode ingest
```
This routine checks your raw data, translates it to embeddings, builds a fast traversal map matching your filesystem, and writes binary output to `faiss_index/`.

### Step 2: Ask a Question
Once digestion completes and FAISS indices sit inside `faiss_index/`, you may issue semantic queries seamlessly:
```bash
python code/main.py --mode query --query "Who is Hanuman?"
```

## Design Decisions

* **Strict CPU constraints:** Prevented out-of-core memory access or expensive GPU allocation by selecting Flan-t5 (~300M parameters).
* **Decoupled System:** Functions are perfectly split. The vector retriever and knowledge generator are cleanly abstracted into separate `.py` services for extreme predictability.
* **Self-Contained DB:** Used `FAISS` with local persistence (`load_local`/`save_local`) instead of heavier networked vector environments (e.g., Pinecone/Chroma server) maximizing modularity.
