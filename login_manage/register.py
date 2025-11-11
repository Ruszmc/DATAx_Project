import getpass
import sqlite3

from data.database import DATABASE_PATH


def register_user():
    user_id = input("Enter the user ID: ")

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT registered_user_id
        FROM login_manage
        WHERE registered_user_id = ?
    ''', (user_id,))


    user_exist = cursor.fetchall()

    if not user_exist:
        print(f"This User ID doesn't exist!")
        conn.close()
        return

    cursor.execute('''
        SELECT user_name, password
        FROM login_manage
        WHERE registered_user_id = ?
        AND user_name IS NOT NULL
        AND password IS NOT NULL
    ''', (user_id,))

    already_registered = cursor.fetchone()

    if already_registered:
        print(f"This User ID is already registered!")
        conn.close()
        return

    username = input("Enter the username: ")
    password = input("Enter the password: ")
##    password = getpass.getpass("Enter the password: ")
##      replace later, so i dont have an error rn

    try:
        cursor.execute('''
            UPDATE login_manage
            SET user_name = ?, password = ?
            WHERE registered_user_id = ?
        ''', (username, password, user_id))

        conn.commit()
        print(f"User {username} registered successfully through {user_id}!")
        print("You can now login_manage with your credentials.")
    except sqlite3.Error as e:
        print(f"Registration failed: {e}")
        conn.rollback()
    finally:
        conn.close()
