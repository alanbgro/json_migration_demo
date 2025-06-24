# JSON Contact Data Migration Tool

This project is a functional prototype developed for a real data migration task posted on Upwork.

It demonstrates how to load, validate, transform, and export contact records stored in `.json` format using Python — with clean code, test coverage, and a modular structure.

## Use Case

Originally built for a freelance client with over 9,000 contact and company records in JSON.  
The objective was to migrate and validate data into a clean format for integration into a CRM system.

## Features

- Load contact data from JSON
- Validate required fields: `full_name`, `email`, `phone`, `company`
- Transform valid entries into a standardized schema
- Export results to:
  - `migrated_output.json`
  - `migrated_output.csv`
- Log invalid/incomplete entries into `validation_log.txt`
- Unit tests included via `unittest`

## Project Structure

```

json\_migration\_demo/
│
├── data/
│   └── contacts\_sample.json          # Sample input
│
├── output/
│   ├── migrated\_output.json          # Exported valid JSON
│   ├── migrated\_output.csv           # Exported valid CSV
│   └── validation\_log.txt            # Log of invalid entries
│
├── src/
│   ├── migration\_script.py           # Main script
│   ├── utils.py                      # Helper functions
│
├── tests/
│   ├── test\_script\_flow\.py           # Full script test
│   ├── test\_migration.py             # Unit tests
│
└── README.md                         # This file

```

## How to Run the Script

1. Make sure Python 3 is installed.
2. Place your input file in `data/contacts_sample.json`.
3. Run the migration script:

```

python src/migration\_script.py

```

4. Outputs will be saved in the `output/` folder.

## How to Run the Tests

```

# Windows

\$env\:PYTHONPATH="src"; python -m unittest discover tests

# Linux/macOS

PYTHONPATH=src python -m unittest discover tests

```

Expected result:

```

Ran 1 test in 0.15s
OK

````

## Sample Input

```json
{
  "full_name": "Jane Doe",
  "email": "jane.doe@example.com",
  "phone": "5551234567",
  "company": "Example Inc."
}
````

## Technologies Used

* Python 3.12.6
* Standard libraries: json, csv, os, unittest
* Clean modular structure and reusable functions

## About the Developer

Developed by alanbgro

GitHub: https://github.com/alanbgro

## License

MIT — free to use and modify.
```
## Notes

This script was created as part of a freelance proposal for a client who needed to migrate approximately 9,000 contact and company records from JSON into a new system. The goal was to ensure data integrity and provide reusable, readable code.

> Output and cache files are excluded from version control using `.gitignore`, ensuring a clean repository focused on source code and test assets only.sssss
