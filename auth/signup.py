import flet as ft
import sqlite3
import bcrypt
import os

# Path to the database
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'database', 'parking.db')

def signup_user(username, password):
    if not username or not password:
        return False, "Username and password required", None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Hash password
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        # Insert into DB
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
        conn.commit()

        # Fetch the newly created user's ID
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = cursor.fetchone()[0]

        return True, "Signup successful", user_id

    except sqlite3.IntegrityError:
        return False, "Username already exists", None
    except Exception as e:
        return False, str(e), None
    finally:
        conn.close()

def signup_view(page: ft.Page, on_success):
    from auth.login import login_view  # avoid circular import issues

    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)
    message = ft.Text(color="red")

    def submit_signup(e):
        success, msg, user_id = signup_user(username.value, password.value)
        message.color = "green" if success else "red"
        message.value = msg
        page.update()

        if success:
            on_success(user_id)  # Now passes user_id to main.py

    page.controls.clear()
    page.add(
        ft.Text("Signup", size=30, weight="bold"),
        username,
        password,
        ft.ElevatedButton("Sign Up", on_click=submit_signup),
        message,
        ft.TextButton("Already have an account? Login here", on_click=lambda e: login_view(page, on_success))
    )
    page.update()
