import sqlite3
import os
import random
import pyttsx3
from utils.distance_calculator import haversine
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

def save_booking(user_id, spot_id, duration_minutes):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
    INSERT INTO bookings (user_id, spot_id, booking_time, duration, status)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, spot_id, datetime.now().isoformat(), duration_minutes, "active"))
    conn.commit()
    conn.close()

def book_parking_spot(user_id, spot_id, duration_minutes):
    save_booking(user_id, spot_id, duration_minutes)
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT empty_slots FROM parking_locations WHERE id=?", (spot_id,))
    row = cursor.fetchone()
    if row:
        empty_slots = row[0]
        if empty_slots > 0:
            new_empty_slots = empty_slots - 1
            cursor.execute('''
                UPDATE parking_locations SET empty_slots = ? WHERE id = ?
            ''', (new_empty_slots, spot_id))

            
            conn.commit()
            conn.close()
            return True, new_empty_slots
    conn.close()
    return False, 0

def fetch_nearest_parking_spots(user_lat, user_lon):
    """
    Returns the top 5 nearest parking locations with slots.
    This is GUI safe – no terminal prompts or bookings inside.
    """
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, name, latitude, longitude, total_slots, empty_slots FROM parking_locations")
        all_spots = cursor.fetchall()

        if not all_spots:
            return []

        distances = []
        for spot in all_spots:
            spot_id, name, lat, lon, total_slots, empty_slots = spot
            dist = haversine(user_lat, user_lon, lat, lon)
            # Simulate slot fluctuation
            new_empty_slots = max(0, min(total_slots, empty_slots + random.randint(-3, 3)))
            cursor.execute("UPDATE parking_locations SET empty_slots = ? WHERE id = ?", (new_empty_slots, spot_id))
            distances.append((dist, spot_id, name, lat, lon, total_slots, new_empty_slots))

        conn.commit()
        distances.sort(key=lambda x: x[0])
        top_5_spots = [spot for spot in distances[:5] if spot[6] > 0]
        return top_5_spots

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    finally:
        conn.close()
