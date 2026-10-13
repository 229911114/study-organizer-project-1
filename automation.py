from storage import load_data


def generate_comprehensive_report():
    """Generates a unified automation report combining tasks, schedule, and notes data."""
    try:
        tasks = load_data("tasks.json")
    except Exception:
        tasks = []

    try:
        schedule = load_data("schedule.json")
    except Exception:
        schedule = []

    try:
        notes = load_data("notes.json")
    except Exception:
        notes = []

    total_tasks = len(tasks)
    pending_tasks = sum(1 for t in tasks if t.get("status") == "Pending")
    completed_tasks = total_tasks - pending_tasks

    total_schedule = len(schedule)
    total_notes = len(notes)

    report = (
        "\n========================================\n"
        "       STUDY ORGANIZER AUTOMATION REPORT       \n"
        "========================================\n"
        f"Assignments & Tasks:\n"
        f"  - Total Tasks: {total_tasks}\n"
        f"  - Pending: {pending_tasks}\n"
        f"  - Completed: {completed_tasks}\n\n"
        f"Study Schedule:\n"
        f"  - Total Scheduled Blocks: {total_schedule}\n\n"
        f"Study Notes:\n"
        f"  - Total Saved Notes: {total_notes}\n"
        "========================================\n"
    )
    return report


def run_automation():
    """Executes the automated reporting workflow and displays the system overview."""
    print("Running automated system integration check...")
    report = generate_comprehensive_report()
    print(report)


if __name__ == "__main__":
    run_automation()
