import argparse
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
from loader import load_documents
from chunker import chunk_documents
from embedder import get_embedder
from vector_store import build_vector_store, load_vector_store
from retriever import get_retriever
from generator import get_llm
from rag_pipeline import build_rag_pipeline
import logging

# Suppress verbose warnings
logging.getLogger("transformers").setLevel(logging.ERROR)


def ingest_data(data_dir, index_path):
    print(f"Loading documents strictly from {data_dir}...")
    docs = load_documents(data_dir)

    if not docs:
        print("No documents found. Add .txt or .pdf files to data/")
        return

    print(f"[DEBUG] Documents loaded: {len(docs)}")

    print("Chunking documents...")
    chunks = chunk_documents(docs)
    print(f"[DEBUG] Chunks created: {len(chunks)}")

    print("Initializing embedder...")
    embedder = get_embedder()

    sample_embedding = embedder.embed_query("test")
    print(f"[DEBUG] Embedding dimension: {len(sample_embedding)}")

    print("Building FAISS index...")
    vector_store = build_vector_store(chunks, embedder, index_path)

    print(f"[DEBUG] FAISS index size: {vector_store.index.ntotal}")
    print("✅ Ingestion complete!")


def query_system(index_path, query):
    print("Loading vector store...")

    embedder = get_embedder()
    vector_store = load_vector_store(embedder, index_path)

    if vector_store is None:
        print("❌ Run ingestion first using --mode ingest")
        return

    retriever = get_retriever(vector_store, k=3)
    generator = get_llm()

    # ✅ NEW lightweight RAG pipeline
    rag = build_rag_pipeline(retriever, generator)

    print(f"\n--- QUERY ---\n{query}\n")

    # Run pipeline
    answer = rag(query)

    print(f"\n--- FINAL ANSWER ---\n{answer}\n")
    print("-" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sanskrit RAG System (CPU)")
    parser.add_argument("--mode", type=str, choices=["ingest", "query", "demo"], required=True)
    parser.add_argument("--data_dir", type=str, default="data")
    parser.add_argument("--index_path", type=str, default="faiss_index")
    parser.add_argument("--query", type=str, default="")

    args = parser.parse_args()

    if args.mode == "ingest":
        if not os.path.exists(args.data_dir):
            os.makedirs(args.data_dir)
        ingest_data(args.data_dir, args.index_path)

    elif args.mode == "query":
        if not args.query:
            parser.error("--query required for query mode")
        query_system(args.index_path, args.query)

    elif args.mode == "demo":
        print("====== DEMO ======")
        queries = [
            "कः गोवर्धनदासः?",
            "घण्टाकर्णः कः?",
            "कालीदासस्य कथा का?"
        ]
        for q in queries:
            query_system(args.index_path, q)