import sqlite3

conn = sqlite3.connect('parking.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM parking_locations")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
