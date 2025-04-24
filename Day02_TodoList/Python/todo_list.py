tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
