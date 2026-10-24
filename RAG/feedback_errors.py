import sqlite3

conn = sqlite3.connect("feedback_practice.db")
conn.execute("PRAGMA foreign_keys = ON")

# পরীক্ষা ১: ভুল rating (5)
try:
    conn.execute(
        "INSERT INTO feedback (answer_id, user_id, rating) VALUES (?, ?, ?)",
        (1, 2, 5),
    )
except sqlite3.IntegrityError as e:
    print("পরীক্ষা ১ আটকেছে:", e)

# পরীক্ষা ২: একই user একই answer-এ দ্বিতীয়বার feedback
try:
    conn.execute(
        "INSERT INTO feedback (answer_id, user_id, rating) VALUES (?, ?, ?)",
        (1, 1, -1),
    )
except sqlite3.IntegrityError as e:
    print("পরীক্ষা ২ আটকেছে:", e)

# পরীক্ষা ৩: যে answer_id-ই নেই
try:
    conn.execute(
        "INSERT INTO feedback (answer_id, user_id, rating) VALUES (?, ?, ?)",
        (999, 1, 1),
    )
except sqlite3.IntegrityError as e:
    print("পরীক্ষা ৩ আটকেছে:", e)

conn.close()
