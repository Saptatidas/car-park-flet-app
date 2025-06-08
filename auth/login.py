import flet as ft
import sqlite3
import bcrypt
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')

def login_user(username, password):
    if not username or not password:
        return False, None, "Username and password required"
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            return False, None, "User not found"
        user_id, pw_hash = user
        if bcrypt.checkpw(password.encode(), pw_hash):
            return True, user_id, "Login successful"
        else:
            return False, None, "Wrong password"
    except Exception as e:
        return False, None, str(e)
    finally:
        conn.close()

def login_view(page: ft.Page, on_success):
    from auth.signup import signup_view  # moved inside to avoid circular import

    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    message = ft.Text(color="red")

    def submit_login(e):
        success, user_id, msg = login_user(username.value, password.value)
        message.color = "green" if success else "red"
        message.value = msg
        page.update()
        if success:
            on_success(user_id)

    page.controls.clear()
    page.add(
        ft.Text("Login", size=30, weight="bold"),
        username,
        password,
        ft.ElevatedButton("Login", on_click=submit_login),
        message,
        ft.TextButton("Don't have an account? Signup here", on_click=lambda e: signup_view(page, on_success))
    )
    page.update()
