import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import is_valid, transform


class TestMigrationFunctions(unittest.TestCase):

    def setUp(self):
        self.valid_contact = {
            "name": "Alice Doe",
            "email": "alice@example.com",
            "phone": "+1-234-567-8901",
            "company": "TestCorp"
        }

        self.invalid_contact = {
            "name": "Bob",
            "email": "",
            "phone": "",
            "company": "NoPhoneCorp"
        }

        self.original_contact = {
            "name": "Alice Doe",
            "email": "alice@example.com",
            "phone": "1234567890",
            "company": "Example Inc."
        }

        self.expected_transformed = {
            "full_name": "Alice Doe",
            "email": "alice@example.com",
            "phone_number": "1234567890",
            "organization": "Example Inc."
        }

    def test_valid_contact(self):
        self.assertTrue(is_valid(self.valid_contact))

    def test_invalid_contact(self):
        self.assertFalse(is_valid(self.invalid_contact))

    def test_transform_contact(self):
        self.assertEqual(transform(self.original_contact), self.expected_transformed)


if __name__ == '__main__':
    unittest.main()
