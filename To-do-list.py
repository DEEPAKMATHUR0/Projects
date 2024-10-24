# To-Do List Manager in Python

def display_menu():
    print("\n----- To-Do List Manager -----")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔ Completed" if task['completed'] else "✘ Not Completed"
            print(f"{idx}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append({'task': task, 'completed': False})
    print(f"Task '{task}' added.")

def mark_task_completed(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to complete.")
    else:
        view_tasks(tasks)
        try:
            task_no = int(input("\nEnter the task number you want to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]['completed'] = True
                print(f"Task '{tasks[task_no - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to remove.")
    else:
        view_tasks(tasks)
        try:
            task_no = int(input("\nEnter the task number you want to remove: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print(f"Task '{removed_task['task']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("\nExiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
