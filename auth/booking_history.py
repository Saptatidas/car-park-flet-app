import sqlite3
import os
from datetime import datetime, timedelta
import flet as ft

def view_booking_history(page: ft.Page, user_id, open_dashboard_func):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')

    # Header
    header = ft.Text("🕓 Your Parking Booking History", size=22, weight="bold", color="#4e342e")

    # Scrollable list view
    list_view = ft.ListView(expand=True, spacing=10, padding=10)

    # Connect to DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT b.booking_time, b.duration, b.status, p.name
        FROM bookings b
        JOIN parking_locations p ON b.spot_id = p.id
        WHERE b.user_id = ?
        ORDER BY b.booking_time DESC
    ''', (user_id,))
    bookings = cursor.fetchall()
    conn.close()

    if not bookings:
        list_view.controls.append(
            ft.Text("📭 You have no booking history.", size=16, color="gray")
        )
    else:
        now = datetime.now()
        for i, (booking_time, duration, status, spot_name) in enumerate(bookings, start=1):
            start_time = datetime.fromisoformat(booking_time)
            end_time = start_time + timedelta(minutes=duration)

            if status == "active" and now > end_time:
                display_status = "⛔ Expired"
            elif status == "active":
                display_status = "✅ Active"
            else:
                display_status = "✔ Completed"

            # Booking item block
            list_view.controls.extend([
                ft.Text(f"{i}. 📍 {spot_name}", weight="bold", size=16, color="#1b5e20"),
                ft.Text(f"   ⏰ Start: {start_time.strftime('%Y-%m-%d %H:%M')}", size=14),
                ft.Text(f"   🕓 Duration: {duration} minutes", size=14),
                ft.Text(f"   🚦 Status: {display_status}", size=14, color="#147a8c"),
                ft.Divider()
            ])

    # Back button to dashboard
    def close_page(e):
        page.controls.clear()
        open_dashboard_func()  # Call the callback passed
        page.update()

    close_button = ft.ElevatedButton("🔙 Back to Dashboard", on_click=close_page, bgcolor="#8e24aa", color="white")

    # Final page render
    page.controls.clear()
    page.controls.extend([
        header,
        list_view,
        ft.Container(close_button, alignment=ft.alignment.center)
    ])
    page.update()
