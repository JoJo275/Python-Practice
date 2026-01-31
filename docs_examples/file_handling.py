"""
File Handling in Python
=======================

Essential patterns for reading, writing, and managing files.
"""

import os
from pathlib import Path

# 1. Reading Files
print("=== Reading Files ===")

# Using context manager (recommended)
# with open("example.txt", "r") as f:
#     content = f.read()          # Read entire file
#     lines = f.readlines()       # Read as list of lines
#     line = f.readline()         # Read single line

# Reading methods comparison
sample_text = "Line 1\nLine 2\nLine 3"
print(f"Sample text:\n{sample_text}\n")


# 2. Writing Files
print("=== Writing Files ===")

# Write modes:
# 'w'  - Write (overwrites existing)
# 'a'  - Append (adds to end)
# 'x'  - Exclusive create (fails if exists)
# 'r+' - Read and write

write_modes = {
    'w': 'Write - overwrites file',
    'a': 'Append - adds to end',
    'x': 'Exclusive - fails if exists',
    'r+': 'Read/Write - both operations',
    'wb': 'Write binary',
    'rb': 'Read binary',
}

for mode, desc in write_modes.items():
    print(f"  '{mode}': {desc}")


# 3. Working with Paths (pathlib - modern approach)
print("\n=== Path Operations (pathlib) ===")

current = Path.cwd()
print(f"Current directory: {current}")

# Path manipulation
example_path = Path("/users/documents/file.txt")
print(f"Parent: {example_path.parent}")
print(f"Name: {example_path.name}")
print(f"Stem: {example_path.stem}")
print(f"Suffix: {example_path.suffix}")

# Building paths
new_path = Path("folder") / "subfolder" / "file.py"
print(f"Built path: {new_path}")


# 4. Directory Operations
print("\n=== Directory Operations ===")

# Common os operations
os_operations = """
os.getcwd()          - Get current working directory
os.chdir(path)       - Change directory
os.listdir(path)     - List directory contents
os.mkdir(path)       - Create single directory
os.makedirs(path)    - Create nested directories
os.remove(file)      - Delete file
os.rmdir(dir)        - Delete empty directory
os.path.exists(path) - Check if path exists
os.path.isfile(path) - Check if it's a file
os.path.isdir(path)  - Check if it's a directory
"""
print(os_operations)


# 5. Safe File Operations Pattern
print("=== Safe File Operations ===")

def safe_read_file(filepath):
    """Safely read a file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Demo
result = safe_read_file("nonexistent.txt")
print(f"Result: {result}")


# 6. Working with CSV (quick reference)
print("\n=== CSV Quick Reference ===")
csv_example = '''
import csv

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading as dictionary
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column_name"])

# Writing CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["col1", "col2"])
    writer.writerows(data)
'''
print(csv_example)


# 7. Working with JSON
print("=== JSON Quick Reference ===")
json_example = '''
import json

# Reading JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Writing JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# String conversion
json_string = json.dumps(data)
data = json.loads(json_string)
'''
print(json_example)


if __name__ == "__main__":
    print("\n✅ File handling guide executed successfully!")
