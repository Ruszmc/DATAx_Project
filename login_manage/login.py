import getpass
import sqlite3

from data.database import DATABASE_PATH
from tasks.user_management import add_user, del_user
from tasks.task_management import add_task, show_tasks_from_user


def login_user():
    from main import main_menu
    user = input("Username: ")
    password = input("Password: ")

    if user == "Fynn":
        if password == "test":
            print("Welcome to the randomass database!")

            while True:
                print("What would you like to do?")
                print("1. Add user")
                print("2. Delete user")
                print("3. logout")
                print("4. Add task")
                print("5. Show tasks from user")
                print("6. Exit")
                choice = input("Input number: ")
                if choice == "1":
                    add_user()
                elif choice == "2":
                    del_user()
                elif choice == "3":
                    main_menu()
                    break
                elif choice == "4":
                    add_task()
                elif choice == "5":
                    show_tasks_from_user()
                elif choice == "6":
                    print("Goodbye!")
                    exit()
        else:
            print("Wrong username or password!")
            return login_user()
    else:
        print("Wrong username or password!")
        return login_user()


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

    if not user_exist:
        print(f"This User doesn't exist or hasn't been registered yet!")
        conn.close()
        return

