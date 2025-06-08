# db/init_users.py
import sqlite3

conn = sqlite3.connect('parking.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT
)
""")
conn.commit()
conn.close()
print("✅ users table created.")
