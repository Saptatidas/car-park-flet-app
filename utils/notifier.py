import sqlite3
import os
import time
from datetime import datetime, timedelta
import threading
from queue import Queue

# Queue to send expired booking info to main.py
alert_queue = Queue()

def get_alert_queue():
    return alert_queue

def start_booking_notifier():
    def monitor():
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')
        while True:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            now = datetime.now()

            cursor.execute("""
                SELECT b.id, b.user_id, b.booking_time, b.duration, p.name
                FROM bookings b
                JOIN parking_locations p ON b.spot_id = p.id
                WHERE b.status = 'active'
            """)
            bookings = cursor.fetchall()

            for booking_id, user_id, booking_time, duration, spot_name in bookings:
                try:
                    start_time = datetime.fromisoformat(booking_time)
                    end_time = start_time + timedelta(minutes=duration)

                    if now >= end_time:
                        # ⚠️ Do NOT mark expired here — let user decide in main.py
                        alert_queue.put({
                            'booking_id': booking_id,
                            'user_id': user_id,
                            'spot_name': spot_name
                        })
                except Exception as e:
                    print(f"⚠️ Error processing booking #{booking_id}: {e}")

            conn.close()
            time.sleep(60)  # check every 1 min

    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
