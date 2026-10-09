from pathlib import Path
import json

# Find the main project folder
BASE_DIR = Path(__file__).resolve().parent

# Create a path to the data folder
DATA_DIR = BASE_DIR / "data"


def initialize_app():
    # Create the data folder if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Define the files our app needs
    files = {
        "tasks.json": [],
        "schedule.json": [],
        "notes.json": []
    }

    # Create any files that are missing
    for filename, default_data in files.items():
        file_path = DATA_DIR / filename

        if not file_path.exists():
            with file_path.open("w", encoding="utf-8") as file:
                json.dump(default_data, file, indent=4)

    print("Study Organizer is ready!")


if __name__ == "__main__":
    initialize_app()