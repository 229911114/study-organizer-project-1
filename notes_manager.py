import json
from pathlib import Path
from storage import load_data, save_data


def add_note(notes):
    """Prompts user to add a new note and appends it to the list."""
    title = input("Enter note title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return False
    
    content = input("Enter note content: ").strip()
    notes.append({"title": title, "content": content})
    print("Note added successfully!")
    return True


def view_notes(notes):
    """Displays all current notes."""
    if not notes:
        print("No notes available.")
        return
    
    print("\n--- YOUR STUDY NOTES ---")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note['title']}")
        print(f"   {note['content']}")
        print("-" * 20)


def search_note(notes):
    """Searches notes by keyword in title or content."""
    keyword = input("Enter search keyword: ").strip().lower()
    if not keyword:
        print("Search keyword cannot be empty.")
        return
    
    matches = [
        note for note in notes
        if keyword in note["title"].lower() or keyword in note["content"].lower()
    ]
    if matches:
        view_notes(matches)
    else:
        print("No matching notes found.")


def choose_note(notes):
    """Helper to select a specific note by index."""
    view_notes(notes)
    if not notes:
        return None
    
    try:
        number = int(input("Enter note number: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return None
    
    if not 1 <= number <= len(notes):
        print("Invalid note number.")
        return None
    
    return number - 1


def edit_note(notes):
    """Edits an existing note's title or content."""
    index = choose_note(notes)
    if index is None:
        return False
    
    title = input("New title (Enter to keep old): ").strip()
    content = input("New content (Enter to keep old): ").strip()
    
    if not title and not content:
        print("No changes made.")
        return False
    
    if title:
        notes[index]["title"] = title
    if content:
        notes[index]["content"] = content
        
    print("Note updated successfully!")
    return True


def delete_note(notes):
    """Deletes a note by its listed number."""
    index = choose_note(notes)
    if index is None:
        return False
    
    deleted = notes.pop(index)
    print(f"Deleted: {deleted['title']}")
    return True


def run_notes_manager():
    """Main CLI loop for the Notes Manager, integrating team storage."""
    filename = "notes.json"
    
    # Load existing notes using the team's storage module
    try:
        notes = load_data(filename)
    except (FileNotFoundError, ValueError):
        notes = []

    def save_callback(items):
        save_data(filename, items)

    while True:
        print("\n===== NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Return to Main Menu")
        
        choice = input("Choose an option (1-6): ").strip()
        changed = False

        if choice == "1":
            changed = add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_note(notes)
        elif choice == "4":
            changed = edit_note(notes)
        elif choice == "5":
            changed = delete_note(notes)
        elif choice == "6":
            print("Exiting Notes Manager...")
            break
        else:
            print("Invalid choice. Try again.")

        if changed:
            try:
                save_callback(notes)
            except OSError as error:
                print(f"Warning: Could not save notes: {error}")


if __name__ == "__main__":
    run_notes_manager()
