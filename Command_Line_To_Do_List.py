import os
import json

class ToDo:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f'Task "{task}" added!')

    def delete_task(self, task_index):
        """Delete a task from the list."""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f'Task "{removed_task["task"]}" deleted!')
        else:
            print("Invalid task index!")

    def mark_completed(self, task_index):
        """Mark a task as completed."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed!')
        else:
            print("Invalid task index!")

    def view_tasks(self):
        """View all tasks with their status."""
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{idx + 1}. {task['task']} [{status}]")

    def save_tasks(self):
        """Save the tasks to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        """Load tasks from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

def menu():
    print("\n=== Command-Line To-Do List ===")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Exit")

def main():
    todo = ToDo()

    while True:
        menu()
        choice = input("\nEnter your choice: ").strip()

        match choice:
            case '1':
                todo.view_tasks()

            case '2':
                task = input("Enter a new task: ").strip()
                if task:
                    todo.add_task(task)
                else:
                    print("Task cannot be empty.")

            case '3':
                todo.view_tasks()
                task_index = input("Enter the task number to delete: ").strip()
                # Check if the input is a valid number
                if task_index.isdigit():
                    todo.delete_task(int(task_index) - 1)  # Convert string to integer for indexing
                else:
                    print("Please enter a valid number.")

            case '4':
                todo.view_tasks()
                task_index = input("Enter the task number to mark as completed: ").strip()
                # Check if the input is a valid number
                if task_index.isdigit():
                    todo.mark_completed(int(task_index) - 1)  # Convert string to integer for indexing
                else:
                    print("Please enter a valid number.")

            case '5':
                print("Exiting the program.")
                break

            case _:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
