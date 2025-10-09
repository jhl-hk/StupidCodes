# Create a simple to-do list where users can add, remove, or mark tasks as completed. 
# Use a file to store the tasks so they persist after the program is closed.

import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

def remove_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

def mark_task_completed(tasks, index):
    tasks[index]["completed"] = True
    save_tasks(tasks)

def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"\nTask List")
        print(f"----------")
        print(f"{index}. {task['task']} - {status}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, index - 1)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_task_completed(tasks, index - 1)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()