import unittest
import json

from setup import initialize_app, DATA_DIR
from storage import load_data, save_data


class TestStorage(unittest.TestCase):

    def setUp(self):
        initialize_app()

    def test_save_and_load(self):
        sample = [
            {"id": 1, "title": "Math homework"}
        ]

        save_data("tasks.json", sample)
        result = load_data("tasks.json")

        self.assertEqual(result, sample)

    def test_invalid_filename(self):
        with self.assertRaises(ValueError):
            save_data("../other.json", [])

    def test_invalid_json(self):
        file_path = DATA_DIR / "tasks.json"

        original = file_path.read_text(encoding="utf-8")

        try:
            file_path.write_text(
                "{invalid json",
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):
                load_data("tasks.json")
        finally:
            file_path.write_text(
                original,
                encoding="utf-8"
            )

if __name__ == "__main__":
    unittest.main()