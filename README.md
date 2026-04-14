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
├── code/
│   ├── rag_pipeline.py
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── generator.py
│   └── requirements.txt
│
├── data/
│   └── Rag-docs.txt
│
├── report/
│
└── README.md
```

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

## Sample Input and Output

====== DEMO ======

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

## Limitations
- Limited reasoning ability
- Dependent on dataset
- Small model constraints

## Future Improvements
- Better Indic embeddings
- GPU support
- Web interface (Streamlit/Gradio)
- OCR integration

## Author
- Arya
