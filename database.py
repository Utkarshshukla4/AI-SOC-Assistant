import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os


# --------------------------------------------------
# Database Path
# --------------------------------------------------

DATABASE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "users.db"
)


# --------------------------------------------------
# Create Database
# --------------------------------------------------

def init_db():

    # Make sure data folder exists
    os.makedirs(
        os.path.dirname(DATABASE),
        exist_ok=True
    )

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# --------------------------------------------------
# Create User
# --------------------------------------------------

def create_user(username, password):

    try:

        connection = sqlite3.connect(DATABASE)

        cursor = connection.cursor()

        hashed_password = generate_password_hash(
            password
        )

        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, hashed_password)
        )

        connection.commit()
        connection.close()

        return True

    except sqlite3.IntegrityError:

        return False

    except Exception as error:

        print("Create user error:", error)

        return False


# --------------------------------------------------
# Verify Login
# --------------------------------------------------

def verify_user(username, password):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    if user:

        return check_password_hash(
            user[0],
            password
        )

    return False


# --------------------------------------------------
# Change Password
# --------------------------------------------------

def update_password(username, new_password):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    hashed_password = generate_password_hash(
        new_password
    )

    cursor.execute(
        """
        UPDATE users
        SET password = ?
        WHERE username = ?
        """,
        (hashed_password, username)
    )

    connection.commit()

    updated = cursor.rowcount > 0

    connection.close()

    return updated