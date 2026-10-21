import os
from dotenv import load_dotenv

load_dotenv()  

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
TOP_K = 4
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHROMA_PATH = "./chroma_db"

# --- Secrets/env-driven ---
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.1-flash-lite")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# vectorstore.py
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
# from config import EMBEDDING_MODEL, CHROMA_PATH


def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
    )


