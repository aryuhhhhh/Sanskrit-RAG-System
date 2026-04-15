# Sanskrit Document Retrieval-Augmented Generation (RAG) System

## Project Description
The Sanskrit Document Retrieval-Augmented Generation (RAG) System is a specialized, CPU-based pipeline designed to intelligently process, retrieve, and answer queries based on Sanskrit text documents. Built to operate entirely offline locally, the system does not require GPUs or external API integrations.

## Features
- Modular pipeline (Loader, Chunker, Embedder, Retriever, Generator)
- Sanskrit-aware preprocessing (handling "।" and "॥")
- FAISS-based vector search
- Lightweight models (MiniLM + Flan-T5-small)
- Anti-hallucination prompt design
- Fully CPU-compatible

## Dataset

The dataset consists of Sanskrit narrative texts (stories and subhashitas).

- Source: Provided assignment documents
- Format: Plain text (.txt)
- Characteristics:
  - Use of "।" and "॥" as sentence delimiters
  - Complex sentence structures
  - Classical Sanskrit vocabulary

## Tech Stack
- Python
- LangChain
- FAISS
- SentenceTransformers (MiniLM)
- HuggingFace Transformers (Flan-T5-small)

## Project Structure
```text
RAG_Sanskrit_Arya/
│
├── code/                          # Core RAG pipeline implementation
│   ├── rag_pipeline.py            # Main execution script
│   ├── loader.py                  # Loads Sanskrit documents
│   ├── chunker.py                 # Splits text using Sanskrit delimiters
│   ├── embedder.py                # Generates embeddings (MiniLM)
│   ├── generator.py               # LLM-based answer generation (Flan-T5)
│   └── requirements.txt           # Dependencies
│
├── data/                          # Input Sanskrit corpus
│   └── Rag-docs.txt
│
├── colab/                         # Backup runnable version 
│   └── Sanskrit_RAG.ipynb
│
├── report/                        # Technical documentation
│   └── technical_report.pdf
│
└── README.md                      # Setup + usage instructions

## Installation and Setup Instructions

Follow these step-by-step instructions to set up the project on your local machine:

- Clone the repository
- Navigate to project folder
- Create virtual environment
- Activate environment
- Install dependencies using requirements.txt

```bash
python -m venv venv  
venv\Scripts\activate   (Windows)  
pip install -r requirements.txt  
```

## How to Run the Project
- Navigate to code directory
- Run the main pipeline file

```bash
cd code  
python rag_pipeline.py  
```

- The system loads the vector store
- Accepts Sanskrit queries
- Retrieves context
- Generates final answer

  ## Google Colab Execution

A fully functional version of the project is available on Google Colab:

👉 [Open Colab Notebook](https://colab.research.google.com/drive/1riu7ZpEn9LodwjCxxucST4KvUXigSFLh?usp=sharing)

### Key Points
- Runs entirely on CPU (no GPU required)  
- No local setup or dependency installation needed  
- End-to-end execution (document loading → retrieval → generation)  
- Pre-configured environment for smooth and quick evaluation  

This is the recommended way to run the project if local execution faces dependency issues.


## System Architecture

The system follows a standard Retrieval-Augmented Generation (RAG) pipeline:

1. Document Loader → Loads Sanskrit text  
2. Chunker → Splits text using Sanskrit delimiters (।, ॥)  
3. Embedder → Converts chunks into vector embeddings  
4. Retriever → Finds relevant chunks using FAISS similarity search  
5. Generator → Produces final answer using Flan-T5  

Flow:

User Query → Embedding → Retrieval → Context → LLM → Answer
  


## Sample Input and Output


Loading vector store...

--- QUERY ---
गोवर्धनदासः शंखनादं किं आनेतुम् आदिशति?

--- Retrieved Context ---
"अरे शंखनाद, गच्छापणम्, शर्कराम् आनय ।" इति स्वभृत्यम् शंखनादम् गोवर्धनदासः आदिशति । ततः शंखनादः आपणम् गच्छति, शर्कराम् जीर्णे वस्त्रे न्यस्यति च । तस्मात् जीर्णवस्त्रात् मार्गे एव सर्वापि शर्करा स्त्रवति ।

--- FINAL ANSWER ---
गोवर्धनदासः शंखनादं शर्कराम् आनेतुम् आदिशति।

------------------------------------------------------------

Loading vector store...

--- QUERY ---
भोजराज्ञा किं घोषितम्?

--- Retrieved Context ---
घोषितं कदाचित् भोजराज्ञा, यदि कोऽपि कविः मम दरबारे नूतनं काव्यं पठति तर्हि ददामि तस्मै लक्षरुप्यकाणि इति ।

--- FINAL ANSWER ---
यदि कोऽपि कविः दरबारे नूतनं काव्यं पठति तर्हि तस्मै लक्षरुप्यकाणि ददामि इति भोजराज्ञा घोषितम्।

------------------------------------------------------------


## How It Works
- Documents are loaded and split into chunks
- Chunks are converted into embeddings
- Stored in FAISS vector database
- Query is embedded and matched
- Relevant chunks are passed to LLM
- LLM generates Sanskrit answer


## Performance Observations
- Average Latency: ~2–5 seconds per query (CPU)
- Retrieval Quality: Relevant context successfully retrieved for most queries
- Model Size: Lightweight models used for efficient CPU inference
- Resource Usage: Low memory footprint, no GPU required
  

## Limitations
- Limited reasoning due to small language model
- Sanskrit embeddings may not capture full semantic richness
- Performance depends on dataset size and quality
- No fine-tuning on Sanskrit-specific corpora


## Future Improvements
- Better Indic embeddings
- GPU support
- Web interface (Streamlit/Gradio)
- OCR integration

## Author
- Arya Gonnade
