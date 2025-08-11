import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()

PDF_PATH = "./data/medical_info.pdf"
INDEX_PATH = "faiss_index"

def create_faiss_index():
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"PDF file not found at {PDF_PATH}")

    print("Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()

    print("Splitting text...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    print("Creating embeddings & FAISS index...")
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(INDEX_PATH)
    print(f"FAISS index saved at {INDEX_PATH}")

if __name__ == "__main__":
    create_faiss_index()
