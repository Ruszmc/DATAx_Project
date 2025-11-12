from .session import current_session

def real_login():
    user = input("Username: ")
    password = input("Password: ")
    ##password = getpass.getpass("Enter the password: ")

    if current_session.login(user, password):
        print(f"\n✅ Welcome {user}!")
        print(f"Role: {current_session.role}")
        login_menu()
        return True
    else:
        print("\n❌ Wrong username or password!")
        return False

def logout():
    username = current_session.username
    current_session.logout()
    print(f"\n👋 Goodbye {username}! You have been logged out.")

def login_menu():
    print("Welcome to the randomass database!")
    while current_session.is_authenticated:
        print(f'Hello {current_session.username}, you are an {current_session.role}!')
        print("What would you like to do?")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. User Management (Admin Only)")
        print("5. Role Management (Admin Only)")
        print("6. View My Profile")
        print("7. Logout")
        choice = input("Input number: ")
        if choice == "1":
            if current_session.require_login():
                print("Viewing tasks...")
        elif choice == "2":
            if current_session.require_login():
                print("Adding task...")
        elif choice == "3":
            if current_session.require_login():
                print("Deleting task...")
        elif choice == "4":
            if current_session.require_admin():
                from tasks.user_management import user_management_menu
                user_management_menu()
        elif choice == "5":
            if current_session.require_admin():
                from tasks.user_management import add_role
                add_role()
        elif choice == "6":
            if current_session.require_login():
                print(f"\n{current_session.get_info()}")
        elif choice == "7":
            logout()
            break
        else:
            print("Invalid choice!")