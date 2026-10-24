import sqlite3

# feedback_practice.db নামে একটা file তৈরি হবে (না থাকলে)
conn = sqlite3.connect("feedback_practice.db")

# SQLite-এ foreign key চেক চালু করতে হয় (default বন্ধ থাকে)
conn.execute("PRAGMA foreign_keys = ON")

# প্রতিটা answer-এর snapshot
conn.execute("""
CREATE TABLE IF NOT EXISTS answers (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id          INTEGER NOT NULL,
    session_id       TEXT NOT NULL,
    original_query   TEXT NOT NULL,
    rewritten_query  TEXT,
    answer           TEXT NOT NULL,
    retrieved_chunks TEXT,
    prompt_version   TEXT,
    model_name       TEXT,
    created_at       TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

# user-এর feedback
conn.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_id  INTEGER NOT NULL REFERENCES answers(id),
    user_id    INTEGER NOT NULL,
    rating     INTEGER NOT NULL CHECK (rating IN (1, -1)),
    comment    TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (answer_id, user_id)
)
""")

conn.commit()
conn.close()
print("tables created")


