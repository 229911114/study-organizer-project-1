import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

ALLOWED_FILES = {
    "tasks.json",
    "schedule.json",
    "notes.json"
}


def _get_file_path(filename):
    """Return the path for an approved data file."""
    if filename not in ALLOWED_FILES:
        raise ValueError(f"Unsupported data file: {filename}")

    return DATA_DIR / filename


def load_data(filename):
    """Load data from an approved JSON file."""
    file_path = _get_file_path(filename)

    if not file_path.exists():
        raise FileNotFoundError(
            f"{filename} does not exist. Run setup first."
        )

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"{filename} contains invalid JSON."
        ) from error

def save_data(filename, data):
    """Save Python data to an approved JSON file."""
    file_path = _get_file_path(filename)
    temp_path = file_path.with_suffix(".tmp")

    try:
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.write("\n")

        temp_path.replace(file_path)

    finally:
        if temp_path.exists():
            temp_path.unlink()