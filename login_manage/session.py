import getpass
import sqlite3
import hashlib

from data.database import DATABASE_PATH

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Session:

    def __init__(self):
        self.user_id = None
        self.username = None
        self.role = None
        self.is_authenticated = False

    def login(self, username, password):

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        hashed_password = hash_password(password)

        cursor.execute('''
            SELECT user_name, password, role, registered_user_id
            FROM login_manage
            WHERE user_name = ? AND password = ?
        ''', (username, hashed_password))

        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            self.username = user_data[0]
            self.role = user_data[2] if user_data[2] else 'user'
            self.user_id = user_data[3]
            self.is_authenticated = True
            return True
        else:
            return False

    def logout(self):
        self.user_id = None
        self.username = None
        self.role = None
        self.is_authenticated = False

    def is_admin(self):
        return self.is_authenticated and self.role and self.role.lower() == 'admin'

    def is_user(self):
        return self.is_authenticated and self.role and self.role.lower() == 'user'

    def require_login(self):
        if not self.is_authenticated:
            raise Exception("User must be logged in to perform this action.")
            return False
        return True

    def require_admin(self):
        if not self.is_authenticated():
            print("You must be logged in to perform this action.")
            return False
        if not self.is_admin():
            print("You must be an admin to perform this action.")
            print(f"Your current role is: {self.role}")
            return False
        return True

    def get_info(self):
        if self.is_authenticated:
            return f"Logged in as {self.username} ({self.role})"
        return "Not logged in"

current_session = Session()