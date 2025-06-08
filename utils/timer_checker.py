import sqlite3
from datetime import datetime, timedelta
import time

def check_for_expired_bookings():
    while True:
        conn = sqlite3.connect('database/parking.db')
        cursor = conn.cursor()

        now = datetime.now()
        query = """
        SELECT id, user_id, booking_time, duration, status
        FROM bookings
        WHERE status = 'active'
        """

        cursor.execute(query)
        bookings = cursor.fetchall()

        for booking in bookings:
            booking_id, user_id, start_time_str, duration, status = booking
            start_time = datetime.fromisoformat(start_time_str)
            end_time = start_time + timedelta(minutes=duration)

            if now >= end_time:
                print(f"\n🔔 User #{user_id}, your parking time for Booking #{booking_id} has ended.")
                extend = input("Do you want to extend it by 30 minutes? (y/n): ")
                if extend.lower() == 'y':
                    cursor.execute("""
                        UPDATE bookings
                        SET duration = duration + 30
                        WHERE id = ?
                    """, (booking_id,))
                    print("✅ Booking extended by 30 minutes.")
                else:
                    cursor.execute("""
                        UPDATE bookings
                        SET status = 'expired'
                        WHERE id = ?
                    """, (booking_id,))
                    print("🛑 Booking marked as expired.")

        conn.commit()
        conn.close()

        time.sleep(60)  # Check every minute
