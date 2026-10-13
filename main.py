import argparse

from setup import initialize_app

from task_manager import run_task_manager
from schedule_manager import run_schedule_manager


def show_menu():
    print("\n===== STUDY ORGANIZER =====")
    print("1. Manage assignments")
    print("2. Manage study schedule")
    print("3. Manage notes")
    print("4. Run automation")
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
            print("Notes manager is not connected yet.")

        elif choice == "4":
            print("Automation is not connected yet.")

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
    else:
        print(f"Command selected: {args.command}")
        print("This feature will be connected later.")


if __name__ == "__main__":
    main()
