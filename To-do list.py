# -------------------------
# To-Do List Application
# -------------------------

# Global tasks list
tasks = []

# -------------------------
# Show tasks
# -------------------------
def show_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔ Done" if task['done'] else "✘ Not Done"
            print(f"{i}. {task['title']} - {status}")
    print()

# -------------------------
# Add a task
# -------------------------
def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!\n")

# -------------------------
# Mark task as done
# -------------------------
def mark_done():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]['done'] = True
        print("Task marked as done!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# -------------------------
# Update task
# -------------------------
def update_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        new_title = input("Enter new task title: ")
        tasks[task_no - 1]['title'] = new_title
        print("Task updated!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# -------------------------
# Delete task
# -------------------------
def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_no - 1)
        print(f"Task '{deleted['title']}' deleted!\n")
    except (ValueError, IndexError):
        print("Invalid task number!\n")

# -------------------------
# Main program loop
# -------------------------
def main():
    while True:
        print("----- To-Do List Menu -----")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        print()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    main()
