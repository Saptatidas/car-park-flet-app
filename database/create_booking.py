# db/init_bookings.py
import sqlite3

conn = sqlite3.connect('parking.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    spot_id INTEGER,
    booking_time TEXT,
    duration INTEGER,
    status TEXT
)
""")

conn.commit()
conn.close()
print("✅ bookings table created.")
