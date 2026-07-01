import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 4:
                    tasks.append({
                        "id": int(data[0]),
                        "task": data[1],
                        "priority": data[2],
                        "status": data[3]
                    })

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
                f"{task['id']}|{task['task']}|"
                f"{task['priority']}|{task['status']}\n"
            )

def add_task():
    name = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ")

    tasks.append({
        "id": len(tasks) + 1,
        "task": name,
        "priority": priority,
        "status": "Pending"
    })

    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\nID\tTask\t\tPriority\tStatus")
    print("-" * 50)

    for task in tasks:
        print(
            f"{task['id']}\t{task['task']}\t"
            f"{task['priority']}\t\t{task['status']}"
        )

def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_id = int(input("Enter Task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks()
            print("Task completed.")
            return

    print("Task not found.")

def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    task_id = int(input("Enter Task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            for i in range(len(tasks)):
                tasks[i]["id"] = i + 1

            save_tasks()
            print("Task deleted.")
            return

    print("Task not found.")

def statistics():
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["status"] == "Completed":
            completed += 1

    pending = total - completed

    print("\n===== Statistics =====")
    print("Total Tasks:", total)
    print("Completed Tasks:", completed)
    print("Pending Tasks:", pending)

load_tasks()

while True:
    print("\n===== SMART TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        statistics()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")