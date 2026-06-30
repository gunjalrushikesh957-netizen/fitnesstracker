import sqlite3

conn = sqlite3.connect("fitness.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fitness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    steps INTEGER,
    exercise TEXT,
    minutes INTEGER,
    calories INTEGER
)
""")

conn.commit()

def save_data(steps, exercise, minutes, calories):
    cursor.execute(
        "INSERT INTO fitness (steps, exercise, minutes, calories) VALUES (?, ?, ?, ?)",
        (steps, exercise, minutes, calories)
    )
    conn.commit()

def get_data():
    cursor.execute("SELECT * FROM fitness")
    return cursor.fetchall()