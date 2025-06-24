import os
import json
import unittest
from src.migration_script import (
    load_contacts,
    is_valid,
    transform,
    export_to_json,
    export_to_csv,
    log_errors,
)

class TestScriptFlow(unittest.TestCase):
    def setUp(self):
        # Define file paths relative to the current test file
        base_dir = os.path.dirname(__file__)
        self.input_file = os.path.join(base_dir, "test_contacts.json")
        self.output_json = os.path.join(base_dir, "migrated_output.json")
        self.output_csv = os.path.join(base_dir, "migrated_output.csv")
        self.log_file = os.path.join(base_dir, "validation_log.txt")

        # Load contacts and separate them into valid and invalid
        self.contacts = load_contacts(self.input_file)
        self.valid = []
        self.invalid = []

        # Validate and transform contacts
        for contact in self.contacts:
            if is_valid(contact):
                self.valid.append(transform(contact))
            else:
                self.invalid.append(contact)

    def test_exports_and_logs(self):
        # Export valid contacts and log invalid ones
        export_to_json(self.valid, self.output_json)
        export_to_csv(self.valid, self.output_csv)
        log_errors(self.invalid, self.log_file)

        # Verify that output files were created
        self.assertTrue(os.path.exists(self.output_json))
        self.assertTrue(os.path.exists(self.output_csv))
        self.assertTrue(os.path.exists(self.log_file))

        # Ensure the exported JSON file is not empty
        with open(self.output_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertGreater(len(data), 0)

    def tearDown(self):
        # Clean up generated files after the test
        for file in [self.output_json, self.output_csv, self.log_file]:
            if os.path.exists(file):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()
