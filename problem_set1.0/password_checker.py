#! /usr/bin/env python3
"""password_checker.py

Password strength checker (length, uppercase, number, symbol).

"""


def is_strong_password(password: str) -> bool:
    """
    Check if the provided password is strong.

    A strong password is defined as one that is at least 8 characters long,
    contains at least one uppercase letter, one number, and one special symbol.

    Args:
        password: The password string to check.
    Returns:
        True if the password is strong, False otherwise.
    Examples:
        >>> is_strong_password("Password1!")
        True
        >>> is_strong_password("weakpass")
        False
    """

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    return has_upper and has_number and has_symbol


if __name__ == "__main__":
    test_passwords = [
        "Password1!",
        "weakpass",
        "Short1!",
        "NoNumber!",
        "nouppercase1!",
        "NoSymbol1",
        "StrongPass123$"
    ]

    for pwd in test_passwords:
        result = is_strong_password(pwd)
        print(f"Password: {pwd.ljust(15)} Strong: {result}")
