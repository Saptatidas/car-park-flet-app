import flet as ft
from auth.signup import signup_view
from auth.login import login_view
from chatbot.voice_input import listen_for_location
from chatbot.voice_output import speak
from chatbot.chatbot_logic import fetch_nearest_parking_spots, book_parking_spot
from utils.geocode_location import get_coordinates_from_place
from auth.booking_history import view_booking_history

def main(page: ft.Page):
    user_id = None
    page.title = "Kolkata Parking Assistant"
    page.scroll = True
    page.bgcolor = "#e0f7fa"
    page.padding = 20

    def on_signup_success(new_user_id):
        nonlocal user_id
        user_id = new_user_id
        page.snack_bar = ft.SnackBar(ft.Text("✅ Signup successful! Logged in."))
        page.snack_bar.open = True
        page.update()
        open_dashboard()

    def handle_signup(e):
        signup_view(page, on_success=on_signup_success)

    def on_login_success(logged_in_user_id):
        nonlocal user_id
        user_id = logged_in_user_id
        page.snack_bar = ft.SnackBar(ft.Text(f"✅ Logged in as User #{user_id}"))
        page.snack_bar.open = True
        page.update()
        open_dashboard()

    def handle_login(e):
        login_view(page, on_success=on_login_success)

    def open_dashboard():
        page.controls.clear()
        dashboard_list = ft.ListView(expand=True, spacing=10, padding=10)

        #title = ft.Text("Welcome to the Parking Dashboard!", size=22, weight="bold", color="#e65100")

        # Reusable global dialog components
        dialog_dropdown = ft.Dropdown(
            label="Select duration (in minutes)",
            options=[ft.dropdown.Option(str(opt)) for opt in [30, 60, 90, 120, 180, 240, 300]],
            width=300
        )
        dialog_status_text = ft.Text("", size=14)

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Booking"),
            content=ft.Column([dialog_dropdown, dialog_status_text], tight=True),
            actions=[],
            actions_alignment=ft.MainAxisAlignment.END
        )

        page.dialog = dialog  # Set dialog on page once

        def find_parking(e):
            dashboard_list.controls.clear()
            dashboard_list.controls.append(ft.Text("🎤 Listening for your location..."))
            page.update()

            speak("Please say your location.")
            user_input = listen_for_location()

            dashboard_list.controls.clear()

            if user_input:
                coords = get_coordinates_from_place(user_input)
                if coords:
                    lat, lon = coords
                    top_spots = fetch_nearest_parking_spots(lat, lon)

                    if top_spots:
                        speak("Here are the nearest parking spots.")
                        dashboard_list.controls.append(ft.Text("🚗 Nearest Available Parking Spots:", weight="bold", text_align="center"))

                        for spot in top_spots:
                            name = spot[2]
                            avail = spot[6]

                            def make_on_click(s):
                                def on_click_booking(e):
                                    print(f"🟢 Booking clicked for spot: {s[2]}")
                                    
                                    dialog.title = ft.Text(f"Booking: {s[2]}")
                                    dialog_dropdown.value = None
                                    dialog_dropdown.error_text = None
                                    dialog_status_text.value = ""

                                    def close_dialog(_=None):
                                        dialog.open = False
                                        page.update()

                                    def book_now(_):
                                        if dialog_dropdown.value:
                                            duration = int(dialog_dropdown.value)
                                            success, new_avail = book_parking_spot(user_id, s[1], duration)

                                            if success:
                                                msg = f"✅ Spot booked at {s[2]} for {duration} minutes. Left: {new_avail}."
                                            else:
                                                msg = "❌ Booking failed."

                                            speak(msg)
                                            dialog_status_text.value = msg
                                            page.snack_bar = ft.SnackBar(ft.Text(msg))
                                            page.snack_bar.open = True
                                            close_dialog()
                                            page.update()
                                        else:
                                            dialog_dropdown.error_text = "Please select a duration!"
                                            page.update()

                                    dialog.actions = [
                                        ft.ElevatedButton("Book Now", on_click=book_now),
                                        ft.TextButton("Cancel", on_click=close_dialog),
                                    ]

                                    dialog.open = True
                                    if dialog not in page.overlay:
                                        page.overlay.append(dialog)
                                    page.update()
                                    print("🔔 Dialog should now open on desktop/mobile.")

                                return on_click_booking



                            btn = ft.ElevatedButton(
                                f"{name} - {avail} slots",
                                on_click=make_on_click(spot),
                                bgcolor="#4caf50",
                                color="white"
                            )
                            dashboard_list.controls.append(btn)
                    else:
                        speak("No available parking nearby.")
                        dashboard_list.controls.append(ft.Text("❌ No available parking."))
                else:
                    speak("Couldn't understand the location.")
                    dashboard_list.controls.append(ft.Text("❌ Invalid location."))
            else:
                speak("No voice input received.")
                dashboard_list.controls.append(ft.Text("❌ No voice input received."))

            page.update()

        def view_history(e):
            dashboard_list.controls.clear()
            speak("Fetching your booking history.")

            def on_close():
                open_dashboard()

            view_booking_history(page, user_id, on_close)

        def logout(e):
            nonlocal user_id
            user_id = None
            speak("You have been logged out.")
            main(page)

        
        page.controls.extend([

            ft.Container(
                ft.Text("Welcome to the Parking Dashboard!", size=22, weight="bold", color="#e65100"),
                padding=ft.padding.all(20),
                alignment=ft.alignment.center
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton("🌟 Find Parking Spot", on_click=find_parking, bgcolor="#00796b", color="white"),
                    ft.ElevatedButton("📜 View Booking History", on_click=view_history, bgcolor="#5c6bc0", color="white"),
                    ft.ElevatedButton("🚪 Logout", on_click=logout, bgcolor="#d32f2f", color="white"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            dashboard_list
        ])


        page.update()

    # Initial screen
    page.controls.clear()
    page.controls.extend([
        ft.Container(
            ft.Text("Kolkata Parking Assistant", size=26, weight="bold", color="#006064"),
            padding=ft.padding.all(20),
            alignment=ft.alignment.center
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("Signup", on_click=handle_signup, bgcolor="#8e24aa", color="white"),
                ft.ElevatedButton("Login", on_click=handle_login, bgcolor="#3949ab", color="white"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )


    ])
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, host="0.0.0.0",port=60585)


