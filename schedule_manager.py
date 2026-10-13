from storage import load_data, save_data

class ScheduleManager:
    def __init__(self, filename="schedule.json"):
        self.filename = filename
        self.schedule = self.load_schedule()

    def load_schedule(self):
        """Loads schedule entries using the team's shared storage module."""
        try:
            return load_data(self.filename)
        except (FileNotFoundError, ValueError) as error:
            print(f"Notice: {error} Starting with an empty schedule list.")
            return []

    def save_schedule(self):
        """Saves schedule entries using the team's shared storage module (atomic write)."""
        save_data(self.filename, self.schedule)

    def add_entry(self, day, time_slot, subject, activity):
        """Adds a new study schedule block."""
        entry = {
            "id": len(self.schedule) + 1,
            "day": day.capitalize(),
            "time_slot": time_slot,
            "subject": subject,
            "activity": activity
        }
        self.schedule.append(entry)
        self.save_schedule()
        print(f"Schedule entry for {entry['day']} ({subject}) added successfully!")

    def list_schedule(self):
        """Displays all recorded schedule blocks in the CLI."""
        if not self.schedule:
            print("\nNo schedule entries found in your study organizer.")
            return
        
        print("\n--- YOUR STUDY SCHEDULE ---")
        for entry in self.schedule:
            print(f"[{entry['id']}] {entry['day']} | {entry['time_slot']}")
            print(f"    Subject: {entry['subject']}")
            print(f"    Activity: {entry['activity']}")
            print("-" * 30)

    def delete_entry(self, entry_id):
        """Deletes a schedule entry by its ID and re-indexes remaining entries."""
        initial_length = len(self.schedule)
        self.schedule = [entry for entry in self.schedule if entry["id"] != entry_id]
        
        if len(self.schedule) < initial_length:
            for index, entry in enumerate(self.schedule, start=1):
                entry["id"] = index
            self.save_schedule()
            print(f"Schedule entry {entry_id} deleted successfully.")
        else:
            print(f"Schedule entry with ID {entry_id} not found.")

    # --- AUTOMATION & SCRIPTING HELPERS ---
    def get_entries_by_day(self, day_name):
        """Automation helper: Returns all schedule entries for a specific day."""
        return [entry for entry in self.schedule if entry["day"].lower() == day_name.lower()]

    def generate_schedule_summary(self):
        """Automation helper: Generates a quick text summary of the study schedule."""
        total = len(self.schedule)
        days_covered = set(entry["day"] for entry in self.schedule)
        
        summary = (
            f"=== SCHEDULE SUMMARY REPORT ===\n"
            f"Total Study Blocks: {total}\n"
            f"Days Scheduled: {len(days_covered)} ({', '.join(sorted(days_covered)) if days_covered else 'None'})"
        )
        return summary


def run_schedule_manager():
    """Interactive CLI menu loop for the Schedule Manager."""
    manager = ScheduleManager()

    while True:
        print("\n=== STUDY ORGANIZER: SCHEDULE MANAGER ===")
        print("1. View Full Schedule")
        print("2. Add Schedule Entry")
        print("3. Delete Schedule Entry")
        print("4. View Schedule Summary Report")
        print("5. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            manager.list_schedule()
        elif choice == "2":
            day = input("Enter day of the week (e.g., Monday): ").strip()
            time_slot = input("Enter time slot (e.g., 10:00 - 12:00): ").strip()
            subject = input("Enter subject name (e.g., Differential Equations): ").strip()
            activity = input("Enter activity description (e.g., Lecture & Practice): ").strip()
            manager.add_entry(day, time_slot, subject, activity)
        elif choice == "3":
            manager.list_schedule()
            try:
                entry_id = int(input("Enter schedule entry ID to delete: "))
                manager.delete_entry(entry_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "4":
            print("\n" + manager.generate_schedule_summary())
        elif choice == "5":
            print("Exiting Schedule Manager...")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    run_schedule_manager()
