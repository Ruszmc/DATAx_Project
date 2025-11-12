import sqlite3
import os
from getpass import getpass
import hashlib

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'database.db')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest

def create_admin_user():
    """Create an admin user directly in the database"""

    # Get admin credentials
    username = input("Enter admin username: ")
    password = getpass("Enter admin password: ")

    # Hash the password (adjust this if your system uses a different hashing method)
    hashed_password = hash_password(password)

    # Generate a registered_user_id
    registered_user_id = f"ADMIN_{username.upper()}"

    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Check if user already exists
        cursor.execute("SELECT user_name FROM login_manage WHERE user_name = ?", (username,))
        if cursor.fetchone():
            print(f"User '{username}' already exists!")
            conn.close()
            return

        # Insert admin user
        cursor.execute('''
                       INSERT INTO login_manage (user_name, password, registered_user_id, role)
                       VALUES (?, ?, ?, 'admin')
                       ''', (username, hashed_password, registered_user_id))

        conn.commit()
        conn.close()

        print(f"\n✓ Admin user '{username}' created successfully!")
        print(f"  Username: {username}")
        print(f"  Role: admin")
        print(f"  Registered ID: {registered_user_id}")

    except Exception as e:
        print(f"Error creating admin user: {e}")


if __name__ == "__main__":
    create_admin_user()