from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(
    collection_name= "vector_db_practice",
    persist_directory="./chroma_db",
    embedding_function= embeddings,
)

print(vector_store._collection.count())
