import json
import sqlite3

conn = sqlite3.connect("feedback_practice.db")
conn.execute("PRAGMA foreign_keys = ON")


chunks = [
    {"chunk_id": "attn_p3_c1", "filename": "attention.pdf", "page": 3, "score": 0.82},
    {"chunk_id": "attn_p4_c2", "filename": "attention.pdf", "page": 4, "score": 0.74},
]

cur = conn.execute(
    """
    INSERT INTO answers
        (user_id, session_id, original_query, rewritten_query,
         answer, retrieved_chunks, prompt_version, model_name)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        1,
        "sess-001",
        "attention কী?",
        "What is the attention mechanism?",
        "Attention হলো ...",
        json.dumps(chunks),
        "v1",
        "gemini-3.1-flash-lite",
    ),
)

# ধাপ ২: এই answer-এর id
answer_id = cur.lastrowid
print("answer_id =", answer_id)

# ধাপ ৩: user 👍 দিল
conn.execute(
    "INSERT INTO feedback (answer_id, user_id, rating, comment) VALUES (?, ?, ?, ?)",
    (answer_id, 1, 1, "ভালো ছিল"),
)

conn.commit()

# দুটো table জুড়ে পড়ে দেখি
rows = conn.execute("""
    SELECT a.original_query, a.prompt_version, f.rating, f.comment
    FROM feedback f
    JOIN answers a ON a.id = f.answer_id
    """).fetchall()

for row in rows:
    print(row)

conn.close()
