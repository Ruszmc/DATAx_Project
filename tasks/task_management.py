import sqlite3
from datetime import date

from data.database import DATABASE_PATH

def add_task():

    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    project_name = input("Enter the project name: ")
    description = input("Enter the task description: ")
    due_date_str = input("Enter the due date (DD.MM.YYYY): ")

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT registered_user_id FROM users
        WHERE LOWER(first_name) = ? AND LOWER(last_name) = ?
    ''', (first_name.lower(), last_name.lower()))

    result = cursor.fetchone()
    if not result:
        print(f"User {first_name} {last_name} not found!")
        conn.close()
        return False
    user_id = result[0]

    due_date_iso = None
    days_left = None
    if due_date_str:
        try:
            if '.' in due_date_str:
                day, month, year = map(int, due_date_str.split('.'))
                due_date = date(year, month, day)
            else:
                due_date = date.fromisoformat(due_date_str)
            due_date_iso = due_date.isoformat()
            days_left = (due_date - date.today()).days
        except Exception as e:
            print(f"Invalient Due Date Format: {due_date_str} -> Error: {e}")
            due_date_iso = None
            days_left = None

    try:
        cursor.execute('''
            INSERT INTO data (registered_user_id, project_name , description, due_date)
            Values (?, ?, ?, ?)
        ''', (user_id, project_name, description, due_date_iso))
        conn.commit()

        print(f"Task '{project_name}' for {first_name} {last_name} added!")

        if days_left is not None:
            if days_left < 0:
                print(
                    f"   ➤ Deadline: {due_date_iso} | 🔴 {abs(days_left)} day{'s' if abs(days_left) != 1 else ''} overdue")
            elif days_left == 0:
                print(f"   ➤ Deadline: {due_date_iso} | 🟡 Due today!")
            else:
                print(f"   ➤ Deadline: {due_date_iso} | 🟢 {days_left} day{'s' if days_left != 1 else ''} left")
        else:
            print(f"   ➤ Deadline: none")

        success = True
    except sqlite3.Error as e:
        print(f"Dataerror: {e}")
        conn.rollback()
        success = False
    finally:
        conn.close()

    return success


def show_tasks_from_user():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    if not first_name or not last_name:
        print("First and last name are required!")
        return

    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT registered_user_id
                       FROM users
                       WHERE LOWER(first_name) = ?
                         AND LOWER(last_name) = ?
                       ''', (first_name.lower(), last_name.lower()))

        user = cursor.fetchone()
        if not user:
            print(f"User {first_name} {last_name} not found!")
            return
        user_id = user[0]

        cursor.execute('''
                       SELECT project_name,
                              description,
                              due_date,
                              CASE
                                  WHEN due_date IS NOT NULL
                                      THEN CAST(julianday(due_date) - julianday(date('now')) AS INTEGER)
                                  ELSE NULL
                                  END AS days_left
                       FROM data
                       WHERE registered_user_id = ?
                       ORDER BY due_date NULLS LAST
                       ''', (user_id,))

        tasks = cursor.fetchall()

        if not tasks:
            print(f"No tasks found for {first_name} {last_name}!")
            return
        print(f"\nTasks for {first_name} {last_name}:")
        print("=" * 70)

        for i, task in enumerate(tasks, 1):
            project, desc, due, days_left = task

            due_str = due if due else "No deadline"

            if days_left is not None:
                if days_left < 0:
                    status = f"🔴 {abs(days_left)} day{'s' if abs(days_left) != 1 else ''} overdue"
                elif days_left == 0:
                    status = "🟡 Due today!"
                else:
                    status = f"🟢 {days_left} day{'s' if days_left != 1 else ''} left"
            else:
                status = "⚪ No Deadline"

            print(f"\n{i}. 📌 {project}")
            if desc and desc.strip():
                print(f"   📝 {desc}")
            print(f"   📅 {due_str} | {status}")
            print("\n" + "=" * 70)

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
