
import json
from pathlib import Path

FILE = Path("tasks.json")
tasks = []


def load_tasks():
    global tasks

    if FILE.exists():
        try:
            tasks = json.loads(FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Could not load saved tasks.")
            tasks = []


def save_tasks():
    FILE.write_text(
        json.dumps(tasks, indent=4),
        encoding="utf-8"
    )


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print("Removed:", removed)
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
