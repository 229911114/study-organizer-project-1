from storage import load_data, save_data
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads tasks using the team's shared storage module."""
        try:
            return load_data(self.filename)
        except (FileNotFoundError, ValueError) as error:
            print(f"Notice: {error} Starting with an empty task list.")
            return []

    def save_tasks(self):
        """Saves tasks using the team's shared storage module (with atomic writing)."""
        save_data(self.filename, self.tasks)

    def add_task(self, title, description, due_date):
        """Adds a new study task."""
        # Optional validation for date format YYYY-MM-DD
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Warning: Due date is not in YYYY-MM-DD format, but task will still be added.")

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "Pending"
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def list_tasks(self):
        """Displays all recorded tasks in the CLI."""
        if not self.tasks:
            print("\nNo tasks found in your study organizer.")
            return
        
        print("\n--- YOUR STUDY TASKS ---")
        for task in self.tasks:
            print(f"[{task['id']}] {task['title']} ({task['status']})")
            print(f"    Description: {task['description']}")
            print(f"    Due Date: {task['due_date']}")
            print("-" * 30)

    def complete_task(self, task_id):
        """Marks a specific task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Deletes a task by its ID and re-indexes remaining tasks."""
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        
        if len(self.tasks) < initial_length:
            for index, task in enumerate(self.tasks, start=1):
                task["id"] = index
            self.save_tasks()
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task with ID {task_id} not found.")

    # --- AUTOMATION & SCRIPTING HELPERS ---
    def get_pending_tasks(self):
        """Automation helper: Returns all tasks that are still pending."""
        return [task for task in self.tasks if task["status"] == "Pending"]

    def generate_task_summary(self):
        """Automation helper: Generates a quick text summary for reports or CLI scripts."""
        total = len(self.tasks)
        pending = len(self.get_pending_tasks())
        completed = total - pending
        
        summary = (
            f"=== TASK SUMMARY REPORT ===\n"
            f"Total Tasks: {total}\n"
            f"Pending: {pending}\n"
            f"Completed: {completed}"
        )
        return summary


def run_task_manager():
    """Interactive CLI menu loop for the Task Manager."""
    manager = TaskManager()

    while True:
        print("\n=== STUDY ORGANIZER: TASK MANAGER ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. View Task Summary Report")
        print("6. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            title = input("Enter task title (e.g., Math Assignment): ").strip()
            description = input("Enter brief description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            manager.add_task(title, description, due_date)
        elif choice == "3":
            manager.list_tasks()
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "4":
            manager.list_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "5":
            print("\n" + manager.generate_task_summary())
        elif choice == "6":
            print("Exiting Task Manager...")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 6.")


if __name__ == "__main__":
    run_task_manager()
