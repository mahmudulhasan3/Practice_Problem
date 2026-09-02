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


from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= api_key)

sentences = [
    "The cat is sleeping on the sofa.",
    "A dog is playing in the garden.",
    "My cat loves to chase mice at night.",
    "FastAPI is a modern Python web framework for building APIs.",
    "Python's async support makes FastAPI very fast.",
]
response = client.models.embed_content(
    model= "gemini-embedding-001",
    contents= sentences,
    config= types.EmbedContentConfig(
        output_dimensionality= 256
    )
)
for i, emb in enumerate(response.embeddings):
    print(f"chunk: {i}, {sentences[i]}, {len(emb.values)}")
