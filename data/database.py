import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def init_user_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            registered_user_id TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print('Database for users initialized')

def init_data_db():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            registered_user_id TEXT NOT NULL,
            project_name TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print('Database for data initialized')

def init_login_db():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        Create Table IF NOT EXISTS login_manage (
            user_name TEXT,
            password TEXT,
            registered_user_id TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print('Database for login_manage initialized')