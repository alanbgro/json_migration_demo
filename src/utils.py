import json
import csv
from datetime import datetime

def load_contacts(file_path):
    """
    Load contact data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of contact dictionaries.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def is_valid(contact):
    """
    Check if a contact dictionary has all required fields.

    Args:
        contact (dict): The contact to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    required_fields = ['name', 'email', 'phone', 'company']
    return all(contact.get(field) for field in required_fields)

def transform(contact):
    """
    Transform a contact into a standardized format.

    Args:
        contact (dict): The original contact data.

    Returns:
        dict: Transformed contact data with new field names.
    """
    return {
        "full_name": contact['name'],
        "email": contact['email'],
        "phone_number": contact['phone'],
        "organization": contact['company']
    }

def export_to_json(data, filename='migrated_output.json'):
    """
    Export a list of contacts to a JSON file.

    Args:
        data (list): List of transformed contact dictionaries.
        filename (str): Output filename.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def export_to_csv(data, filename='migrated_output.csv'):
    """
    Export a list of contacts to a CSV file.

    Args:
        data (list): List of transformed contact dictionaries.
        filename (str): Output filename.
    """
    if not data:
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def log_errors(invalid_contacts, filename='validation_log.txt'):
    """
    Log invalid contacts to a text file.

    Args:
        invalid_contacts (list): List of contact dictionaries that failed validation.
        filename (str): Output filename for the log.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Validation Log - {datetime.now()}\n")
        f.write("=" * 40 + "\n")
        for contact in invalid_contacts:
            f.write(json.dumps(contact, ensure_ascii=False) + "\n")
