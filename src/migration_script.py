import sys
import os

# Add src to the Python path to allow relative imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import (
    load_contacts,
    is_valid,
    transform,
    export_to_json,
    export_to_csv,
    log_errors
)

def main():
    """
    Main script for validating, transforming, and exporting contact data.
    """
    # Load raw contacts from input JSON file
    contacts = load_contacts('data/input_contacts.json')

    valid_contacts = []
    invalid_contacts = []

    # Validate and categorize contacts
    for contact in contacts:
        if is_valid(contact):
            valid_contacts.append(transform(contact))
        else:
            invalid_contacts.append(contact)

    # Export valid contacts and log invalid ones
    export_to_json(valid_contacts, 'output/migrated_output.json')
    export_to_csv(valid_contacts, 'output/migrated_output.csv')
    log_errors(invalid_contacts, 'output/validation_log.txt')

    # Final summary output
    print(f"Migration complete: {len(valid_contacts)} valid, {len(invalid_contacts)} invalid")

if __name__ == "__main__":
    main()

