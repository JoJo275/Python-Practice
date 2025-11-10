"""

Ask for a password and verify if it matches a stored one in a csv file.
If it matches, print "Access granted", otherwise print "Access denied".
Check the csv file for password.

"""

import csv
import getpass
import os
import sys


def verify_password(stored_password: str) -> bool:
    """
    Prompt the user for a password and verify it against the stored password.

    Args:
        stored_password: The correct password to verify against.
    Returns:
        True if the entered password matches the stored password, False otherwise.
    """
    entered_password = getpass.getpass("Enter your password: ")
    return entered_password == stored_password


def get_stored_password_from_csv(file_path: str) -> str:
    """
    Retrieve the stored password from a CSV file.
    Args:
        file_path: Path to the CSV file containing the password.
    Returns:
        The stored password as a string.
    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the CSV file is empty or improperly formatted.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        try:
            # Assuming the password is in the first row, first column
            row = next(reader)
            if not row:
                raise ValueError("The CSV file is empty.")
            return row[0]
        except StopIteration:
            raise ValueError("The CSV file is empty.")
        

def main():
    """
    Main function to execute the password verification process.
    """
    csv_file_path = 'passwords.csv'  # Path to the CSV file containing the password

    try:
        stored_password = get_stored_password_from_csv(csv_file_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    if verify_password(stored_password):
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
