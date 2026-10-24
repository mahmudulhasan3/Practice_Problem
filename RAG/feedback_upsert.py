import sqlite3

conn = sqlite3.connect("feedback_practice.db")
conn.execute("PRAGMA foreign_keys = ON")


def save_feedback(conn, answer_id, user_id, rating, comment=None):
    # আগে না থাকলে insert, আগে থাকলে (answer_id + user_id মিললে) update
    conn.execute(
        """
        INSERT INTO feedback (answer_id, user_id, rating, comment)
        VALUES (?, ?, ?, ?)
        ON CONFLICT (answer_id, user_id)
        DO UPDATE SET rating = excluded.rating,
                      comment = excluded.comment
        """,
        (answer_id, user_id, rating, comment),
    )
    conn.commit()


# Step 2-তে user 1, answer 1-এ 👍 (1) দিয়েছিল।
# এখন সে মত বদলে 👎 (-1) দিল:
save_feedback(conn, answer_id=1, user_id=1, rating=-1, comment="মত বদলেছি")

# answer 1-এর জন্য user 1-এর feedback কতগুলো row আছে?
rows = conn.execute(
    "SELECT answer_id, user_id, rating, comment FROM feedback "
    "WHERE answer_id = 1 AND user_id = 1"
).fetchall()

print(rows)
print("row সংখ্যা:", len(rows))

conn.close()
