import json
import os
import logging

DEFAULT_PATH = "data/gradebook.json"


def load_data(path=DEFAULT_PATH):
    """Load gradebook data from a JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info("Data loaded successfully from %s", path)
            return data
    except FileNotFoundError:
        logging.info("Data file not found. Starting with empty data.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in %s", path)
        print("Error: JSON file is corrupted or invalid.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }


def save_data(data, path=DEFAULT_PATH):
    """Save gradebook data to a JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logging.info("Data saved successfully to %s", path)