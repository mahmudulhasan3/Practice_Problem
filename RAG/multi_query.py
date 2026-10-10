# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv
# import os
# from collections import Counter


# load_dotenv()

# llm = ChatGoogleGenerativeAI(
#     model=os.getenv("MODEL_NAME", "gemini-3.1-flash-lite"),
#     temperature=0,
# )
# rewrite_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Given the chat history and the latest user question, rewrite the "
#             "question so it can be understood without the history.\n"
#             "- Do NOT answer the question.\n"
#             "- If it is already standalone, return it unchanged.\n"
#             "- Output only the rewritten question.",
#         ),
#         MessagesPlaceholder(variable_name="chat_history"),  # history এখানে ঢুকবে
#         ("human", "{question}"),
#     ]
# )

# rewrite_chain = rewrite_prompt | llm | StrOutputParser()

# chat_history = [
#     HumanMessage(content="What is BERT?"),
#     AIMessage(content="BERT is a bidirectional Transformer encoder..."),
# ]

# standalone = rewrite_chain.invoke(
#     {
#         "chat_history": chat_history,
#         "question": "How many layers does it have?",
#     }
# )
# print(standalone)


# from collections import Counter
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# multi_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You write search queries for a research-paper search engine.\n"
#             "Given a question, write {n} different search queries that could find "
#             "relevant passages.\n"
#             "- Use different wording and a different angle in each query.\n"
#             "- One query per line. No numbering, no extra text.",
#         ),
#         ("human", "{question}"),
#     ]
# )

# multi_chain = multi_prompt | llm | StrOutputParser()  # Day 92-এর সেই একই pattern


# def generate_queries(question: str, n: int = 3) -> list[str]:
#     raw = multi_chain.invoke({"question": question, "n": n})
#     queries = [line.strip() for line in raw.split("\n") if line.strip()]
#     return [question] + queries[:n]  # original query সবসময় রাখো


# def multi_query_retrieve(question, retriever, n=3, final_k=5):
#     queries = generate_queries(question, n)
#     print("queries:", queries)  # debug: Piece 4-এর ভুল 6

#     counts = Counter()  # chunk কতগুলো query-তে এসেছে
#     doc_by_key = {}  # key → প্রথমবার দেখা Document

#     for q in queries:
#         for doc in retriever.invoke(q):  # প্রতিটা query আলাদা search
#             key = doc.metadata.get("chunk_id") or doc.page_content  # dedup-এর পরিচয়
#             counts[key] += 1
#             doc_by_key.setdefault(key, doc)  # থাকলে ঢোকাবে না → dedup এখানেই

#     # বেশিবার আসা chunk উপরে, তারপর final_k-তে কাটো
#     ranked = sorted(counts.items(), key=lambda kv: -kv[1])[:final_k]
#     return [doc_by_key[key] for key, _ in ranked]

# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # প্রতি query-তে ছোট k

# question = "How does the model remember earlier words?"

# # Step 1: follow-up হলে rewrite (Piece 3-4)
# standalone = get_standalone_query(chat_history, question)

# # Step 2: standalone query থেকে multi-query retrieve
# docs = multi_query_retrieve(standalone, retriever, n=3, final_k=5)

# # Step 3: final prompt-এ ORIGINAL question যাবে (Piece 2)


# import os
# from dotenv import load_dotenv

# load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "Write 3 different search queries for the question below. "
#             "Use different wording in each. One query per line. No numbering.",
#         ),
#         ("human", "{question}"),
#     ]
# )

# chain = prompt | llm | StrOutputParser()

# result = chain.invoke({"question": "How does the model remember earlier words?"})
# print(result)


import os
from collections import Counter
from dotenv import load_dotenv

load_dotenv()  # সবার আগে: .env থেকে API key load করে

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ---------- Setup: LLM ----------
llm = ChatGoogleGenerativeAI(model=os.getenv("MODEL_NAME", "gemini-3.1-flash-lite"), temperature=0)
# ---------- Setup: ছোট demo vector store (real project-এ এটা তোমার আসল store) ----------
docs = [
    Document(
        page_content="Self-attention relates different positions of a single sequence to compute a representation of it.",
        metadata={"chunk_id": "c1"},
    ),
    Document(
        page_content="Positional encoding injects information about the order of tokens in the sequence.",
        metadata={"chunk_id": "c2"},
    ),
    Document(
        page_content="Long-range dependencies are easier to learn because the path length between any two positions is constant.",
        metadata={"chunk_id": "c3"},
    ),
    Document(
        page_content="The model was trained on the WMT 2014 English-German dataset and reached 28.4 BLEU.",
        metadata={"chunk_id": "c4"},
    ),
    Document(
        page_content="Multi-head attention lets the model attend to information from different representation subspaces.",
        metadata={"chunk_id": "c5"},
    ),
    Document(
        page_content="BERT is pre-trained using masked language modeling.",
        metadata={"chunk_id": "c6"},
    ),
]
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    docs, embeddings, collection_name="mq_demo"
)  # in-memory
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})  # প্রতি query-তে ছোট k

# ---------- 7a: LLM থেকে query চাওয়া ----------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Write {n} different search queries for the question below. "
            "Use different wording and a different angle in each. "
            "One query per line. No numbering, no extra text.",
        ),
        ("human", "{question}"),
    ]
)
chain = prompt | llm | StrOutputParser()


def generate_queries(question: str, n: int = 3) -> list[str]:
    raw = chain.invoke({"question": question, "n": n})  # একটা বড় string

    # ---------- 7b: string → list ----------
    lines = [line.strip() for line in raw.split("\n") if line.strip()]
    return [question] + lines[:n]  # original query সবসময় রাখো, LLM-এর সংখ্যা n-এ কাটো


# ---------- 7c + 7d + 7e: search, dedup, ranking ----------
def multi_query_retrieve(question: str, final_k: int = 4):
    queries = generate_queries(question)
    print("\nQueries:")
    for q in queries:
        print("  -", q)

    counts = Counter()  # chunk কতগুলো query-তে এসেছে
    doc_by_id = {}  # chunk_id → Document

    for q in queries:
        results = retriever.invoke(q)  # 7c: প্রতিটা query আলাদা search
        print(f"\n[{q}] →", [d.metadata["chunk_id"] for d in results])
        for doc in results:
            cid = doc.metadata["chunk_id"]
            counts[cid] += 1
            doc_by_id.setdefault(cid, doc)  # 7d: আগে থাকলে আবার ঢোকে না

    ranked = sorted(counts.items(), key=lambda kv: -kv[1])  # 7e: বেশিবার আসা আগে
    print("\nচাঙ্ক কতবার এসেছে:", dict(ranked))
    return [doc_by_id[cid] for cid, _ in ranked[:final_k]]  # final cap


# ---------- Run ----------
final_docs = multi_query_retrieve("How does the model remember earlier words?")

print("\nFinal chunks (prompt-এ যাবে):")
for d in final_docs:
    print(f"  {d.metadata['chunk_id']}: {d.page_content[:60]}...")

llm = ChatGoogleGenerativeAI(
    model_name = os.getenv("MODEL_NAME", "gemini-3.1-flash-lite"), temparature = 0, top_p = 1
)