import argparse

from setup import initialize_app


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
            print("Task manager is not connected yet.")

        elif choice == "2":
            print("Schedule manager is not connected yet.")

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
    else:
        print(f"Command selected: {args.command}")
        print("This feature will be connected later.")


if __name__ == "__main__":
    main()