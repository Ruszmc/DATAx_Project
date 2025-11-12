from data.database import init_login_db, init_user_db, init_data_db
from login_manage.login import login_user, real_login
from login_manage.register import register_user

def main_menu():
    init_user_db()
    init_data_db()
    init_login_db()
    print("\n")


    while True:
        print("Welcome to the task manager!")
        print("What would you like to do?")
        print("1. Login")
        print("2. register")
        print("3. Exit")
        choice = input("Input number: ")
        if choice == "1":
            real_login()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Goodbye!")
            exit()
        elif choice == "4":
            login_user()
        else:
            print("Invalid choice!")

def main():
    main_menu()


if __name__ == '__main__':
    main()
