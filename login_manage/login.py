import getpass
import sqlite3

from data.database import DATABASE_PATH
from tasks.user_management import add_user, del_user, add_role
from tasks.task_management import add_task, show_tasks_from_user


def login_menu():
    from main import main_menu
    print("Welcome to the randomass database!")
    while True:
        print("What would you like to do?")
        print("1. Add user")
        print("2. Delete user")
        print("3. Add role")
        print("4. logout")
        print("5. Add task")
        print("6. Show tasks from user")
        print("7. Exit")
        choice = input("Input number: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            del_user()
        elif choice == "3":
            add_role()
        elif choice == "4":
            main_menu()
            break
        elif choice == "5":
            add_task()
        elif choice == "6":
            show_tasks_from_user()
        elif choice == "7":
            print("Goodbye!")
            exit()


def real_login():
    user = input("Username: ")
    password = input("Password: ")
    ##password = getpass.getpass("Enter the password: ")

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT user_name, password
        FROM login_manage
        WHERE user_name = ? AND password = ?
    ''', (user, password))

    user_exist = cursor.fetchall()
    conn.close()

    if user_exist:
        print(f"Welcome {user}!")
        login_menu()
        return True
    else:
        print("Wrong username or password!")
        return False