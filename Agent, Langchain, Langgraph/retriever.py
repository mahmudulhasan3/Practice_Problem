# from langchain_chroma import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import chromadb

# client = chromadb.PersistentClient(path="./chroma_db")
# # client.delete_collection(name="aaaaaaaa")


# embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# vectorstore = Chroma(
#     collection_name="aaaaaaa",
#     embedding_function=embeddings,
#     persist_directory="./chroma_db",
# )
# vectorstore.add_texts(
#     texts=["তোমার NITER সম্পর্কিত chunk text এখানে...", "আরেকটা chunk..."],
#     metadatas=[{"source": "..."}, {"source": "..."}],
#     ids=["doc1", "doc2"],
# )
# # retriever = vectorestore.as_retriever(
# #     search_type="similarity_score_threshold",
# #     search_kwargs={"k": 3, "score_threshold": 0.7},
# # )

# retriever = vectorstore.as_retriever(
#     search_type="mmr",
#     search_kwargs={"k": 3},
# )

# results = retriever.invoke("NITER CSE admission requirements")

# for doc in results:
#     print(doc.page_content)
#     print(doc.metadata)


from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

texts = [
    "NITER CSE department offers a 4-year BSc in Computer Science and Engineering.",
    "Admission to NITER requires minimum GPA in SSC and HSC examinations.",
    "NITER is affiliated with the University of Dhaka.",
]

metadatas = [
    {"source": "courses.txt"},
    {"source": "admission.txt"},
    {"source": "about.txt"},
]

# embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_texts(
    texts=texts,
    embedding=embeddings,
    metadatas=metadatas,
    collection_name="niter_information",
    persist_directory="./chroma_db",
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

docs = retriever.invoke("What courses does NITER offer?")

for doc in docs:
    print(doc.page_content)
    print(doc.metadata)
