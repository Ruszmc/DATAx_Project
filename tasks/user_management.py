import sqlite3
from datetime import date

from data.database import DATABASE_PATH

def add_user():

    first_name_ip = input("What is your first name? ").split()

    last_name_ip = input("What is your last name? ").split()

    birthdate_input = input("What is your birth date? (DD.MM.YYYY) ").split(".")

    first_name_out = ' '.join(first_name_ip)
    last_name_out = ' '.join(last_name_ip)

    year_age = date.today().year - int(birthdate_input[2])
    month_age = date.today().month - int(birthdate_input[1])

    if month_age < 0:
        year_age = year_age - 1
        month_age = month_age + 12

    print("Hello " + first_name_out + " " + last_name_out + ", you are " + str(year_age) + " years and " + str(
        month_age) + " months old")

    firstname_list = []
    for each in first_name_ip:
        firstname_list.append(each[0])

    lastname_list = []
    for each in last_name_ip:
        lastname_list.append(each[0])

    new_born = birthdate_input[2][-2:]

    firstname_id = ' '.join(firstname_list)
    lastname_id = ' '.join(lastname_list)

    firstname_id_out = firstname_id.replace(" ", "")
    lastname_id_out = lastname_id.replace(" ", "")

    final_id = firstname_id_out.lower() + lastname_id_out.lower() + "_" + str(new_born).lower()

    print("Your ID is: " + final_id.lower())

    birthdate_str = '.'.join(birthdate_input)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        user_data = (first_name_out, last_name_out, birthdate_str, final_id)
        cursor.execute('''
                       INSERT INTO users (first_name, last_name, birthday, registered_user_id)
                       VALUES (?, ?, ?, ?)
                       ''', user_data)

        id_data = (final_id,)
        cursor.execute('INSERT INTO login_manage (registered_user_id) VALUES (?)', id_data)

        conn.commit()
        task_id = cursor.lastrowid
        print(f"User {first_name_out} added successfully")
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
        task_id = None
    finally:
        conn.close()


    return task_id

def del_user():

    print("\nYou can delete a user by: ")
    print("1. ID")
    print("2. Name")
    print("3. Custom ID")
    choice = input("How do you want to delete a user? (ID) ")

    if choice == "1":
        task_id = int(input("Enter the user ID: ").lower())

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT registered_user_id
                       FROM users
                       WHERE user_id = ?
                       ''', (task_id,))

        user = cursor.fetchone()

        cursor.execute('''
            DELETE FROM users WHERE user_id = ?
        ''', (task_id,))


        user_id = user[0]

        cursor.execute('''
                       DELETE
                       FROM data
                       WHERE registered_user_id = ?
                       ''', (user_id,))

        cursor.execute('''
                       DELETE
                       FROM login_manage
                       WHERE registered_user_id = ?
                       ''', (user_id,))

        if cursor.rowcount == 0:
            print(f"No such user found with the given ID {task_id}!")
        else:
            print(f"User {task_id} deleted successfully!")

        conn.commit()
        conn.close()

    elif choice == "2":
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT registered_user_id
                       FROM users
                       WHERE LOWER(first_name) = ?
                         AND LOWER(last_name) = ?
                       ''', (first_name.lower(), last_name.lower()))

        user = cursor.fetchone()

        cursor.execute('''
            DELETE FROM users WHERE first_name = ? AND last_name = ?
        ''', (first_name, last_name))

        user_id = user[0]

        cursor.execute('''
                       DELETE
                       FROM data
                       WHERE registered_user_id = ?
                       ''', (user_id,))

        cursor.execute('''
                       DELETE
                       FROM login_manage
                       WHERE registered_user_id = ?
                       ''', (user_id,))

        if cursor.rowcount == 0:
            print(f"No such user found with the given name {first_name} {last_name}!")
        else:
            print(f"User {first_name} {last_name} deleted successfully!")

        conn.commit()
        conn.close()
    elif choice == "3":
        custom_id = input("Enter the custom ID: ").lower()

        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM users WHERE registered_user_id = ?
        ''', (custom_id,))

        cursor.execute('''
            DELETE FROM data WHERE registered_user_id = ?
        ''', (custom_id,))

        cursor.execute('''
            DELETE FROM login_manage WHERE registered_user_id = ?
        ''', (custom_id,))

        if cursor.rowcount == 0:
            print(f"No such user found with the given custom ID {custom_id}!")
        else:
            print(f"User {custom_id} deleted successfully!")

        conn.commit()
        conn.close()
    else:
        print("Invalid choice!")
