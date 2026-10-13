import argparse

from setup import initialize_app
from task_manager import run_task_manager, TaskManager
from schedule_manager import run_schedule_manager, ScheduleManager
from notes_manager import run_notes_manager  


def show_menu():
    print("\n===== STUDY ORGANIZER =====")
    print("1. Manage assignments")
    print("2. Manage study schedule")
    print("3. Manage notes")
    print("4. Run automation / report")
    print("5. Exit")


def run_menu():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_task_manager()

        elif choice == "2":
            run_schedule_manager()

        elif choice == "3":
            run_notes_manager()  

        elif choice == "4":
            print("\nGenerating Study Organizer Report...")
            try:
                task_mgr = TaskManager()
                sched_mgr = ScheduleManager()
                print("\n" + task_mgr.generate_task_summary())
                print("\n" + sched_mgr.generate_schedule_summary())
            except Exception as e:
                print(f"Could not generate full report: {e}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    parser = argparse.ArgumentParser(
        description="Study Organizer CLI"
    )

    parser.add_argument(
        "command",
        nargs="?",
        choices=["tasks", "schedule", "notes", "report"],
        help="Optional command to run"
    )

    args = parser.parse_args()

    initialize_app()

    if args.command is None:
        run_menu()
    elif args.command == "tasks":
        run_task_manager()
    elif args.command == "schedule":
        run_schedule_manager()
    elif args.command == "notes":
        run_notes_manager()  
    elif args.command == "report":
        print("Generating Automation Report...")
        task_mgr = TaskManager()
        sched_mgr = ScheduleManager()
        print("\n" + task_mgr.generate_task_summary())
        print("\n" + sched_mgr.generate_schedule_summary())
    else:
        print(f"Command selected: {args.command}")
        print("This feature will be connected later.")


if __name__ == "__main__":
    main()
