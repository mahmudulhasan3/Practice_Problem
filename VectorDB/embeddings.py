# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()
# client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

# result = client.models.embed_content(
#     model = "gemini-embedding-001",
#     contents = "I like dog",
#     config = {"task_type":"RETRIVAL-DOCUMENT"}
# )

# vector = result.embeddings[0].values
# print(f"Vector-এর প্রথম 5টা সংখ্যা: {vector[:5]}")
# print(f"Vector-এ মোট কতগুলো সংখ্যা আছে (Dimension): {len(vector)}")


# from google import genai
# from dotenv import load_dotenv
# import os
# from google.genai import types

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)

# chunks = [
#     "Dhaka is the capital of Bangladesh.",
#     "NITER is affiliated with the University of Dhaka.",
#     "FastAPI is a modern Python web framework.",
# ]
# doc_embedding = client.models.embed_content(
#     model="gemini-embedding-001",
#     contents= chunks,
#     config=types.EmbedContentConfig(
#         output_dimensionality=400, task_type="RETRIEVAL_DOCUMENT"
#     ),
# )

# for i, emb in enumerate(doc_embedding.embeddings):
#     print(f"Chunk: {i}, {chunks[i][:5]}, len: {len(emb.values)}")


# from google import genai
# from dotenv import load_dotenv
# from google.genai import types
# import os

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key= api_key)

# sentences = [
#     "The cat is sleeping on the sofa.",
#     "A dog is playing in the garden.",
#     "My cat loves to chase mice at night.",
#     "FastAPI is a modern Python web framework for building APIs.",
#     "Python's async support makes FastAPI very fast.",
# ]
# response = client.models.embed_content(
#     model= "gemini-embedding-001",
#     contents= sentences,
#     config= types.EmbedContentConfig(
#         output_dimensionality= 256
#     )
# )
# for i, emb in enumerate(response.embeddings):
#     print(f"chunk: {i}, {sentences[i]}, {len(emb.values)}")


# import chromadb
# from chromadb.utils import embedding_functions
# import os
# from dotenv import load_dotenv

# load_dotenv()

# google_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# client = chromadb.PersistentClient(path="./chroma_db")

# collection = client.get_or_create_collection(
#     name="university_docs", embedding_function=google_ef
# )

# collection.add(
#     documents=[
#         "Students must attend 75% classes to sit for final exams.",
#         "The library is open from 8 AM to 10 PM.",
#     ],
#     ids=["doc1", "doc2"],
# )
# print("✅ Added successfully")


# import chromadb
# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()


# # আমাদের নিজের Embedding Function — ChromaDB-কে বলে দিচ্ছি
# # text থেকে vector কীভাবে বানাতে হবে
# class GeminiEmbeddingFunction:
#     def __init__(self):
#         self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#     # ChromaDB internally এই method-টাই কল করবে
#     def __call__(self, input):
#         # input হলো text-এর একটা list, প্রতিটার embedding বানাতে হবে
#         result = self.client.models.embed_content(
#             model="gemini-embedding-001",  # embedding-এর জন্য আলাদা model
#             contents=input,
#         )
#         # প্রতিটা embedding-এর শুধু values (numbers-এর list) বের করে দিচ্ছি
#         return [e.values for e in result.embeddings]


# gemini_ef = GeminiEmbeddingFunction()

# client = chromadb.PersistentClient(path="./chroma_db")

# collection = client.get_or_create_collection(
#     name="university_docs", embedding_function=gemini_ef
# )

# collection.add(
#     documents=[
#         "Students must attend 75% classes to sit for final exams.",
#         "The library is open from 8 AM to 10 PM.",
#     ],
#     ids=["doc1", "doc2"],
# )

# print("✅ Added successfully")

from google import genai
from dotenv import load_dotenv
import os
import chromadb

client = chromadb.PersistentClient(path= "./chroma_db")

collection = client.get_or_create_collection(name= "university_docs")

collection.add(
    documents=[
        "Students must attend 75% classes to sit for final exams.",
        "The library is open from 8 AM to 10 PM.",
    ],
    ids= ["doc1","doc2"]
)
result = collection.get(ids=["doc2"])
print(result)
collection.update(
    ids= ["doc2"],
    documents= "I am mahmud"
)
print(collection.get(ids = ["doc2"]))
now = collection.delete(ids = ["doc2"])
print(collection.get(ids=["doc2"]))


collection.upsert(
    ids = ["doc2", "doc4"],
    documents=[
        "I am mahmud",
        "WHat is ai"
    ]
)
print(collection.get(ids=["doc2"]))
print(collection.get(ids=["doc4"]))
