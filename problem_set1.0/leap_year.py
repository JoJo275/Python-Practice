#!/usr/bin/env python3
"""leap_year.py

Determine if a year is a leap year.

A leap year occurs every 4 years, except for years that are divisible by 100,
unless they are also divisible by 400.
"""

import sys
from typing import Optional


def is_leap_year(year: int) -> bool:
    """
    Determine if the given year is a leap year.

    A year is a leap year if it is divisible by 4,
    except for end-of-century years, which must be divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Raises:
        ValueError: If year is not a positive integer.

    Examples:
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2021)
        False
    """
    if year <= 0:
        raise ValueError(f"Year must be positive, got {year}")

    # More concise logic: divisible by 4 AND (not by 100 OR by 400)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_valid_year() -> Optional[int]:
    """
    Get a valid year from user input with error handling.

    Returns:
        Valid year as integer, or None if user wants to quit.
    """
    while True:
        try:
            user_input = input("Enter a year (or 'quit' to exit): ").strip()

            if user_input.lower() in ('quit', 'q', 'exit'):
                return None

            year = int(user_input)

            if year <= 0:
                print(f"Error: Year must be positive. You entered {year}.")
                continue

            return year

        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer.")
        except KeyboardInterrupt:
            print("\n\nInterrupted by user.")
            return None


def main() -> None:
    """Main function to run the leap year checker."""
    print("="*50)
    print("LEAP YEAR CHECKER")
    print("="*50)

    year = get_valid_year()

    if year is None:
        print("Goodbye!")
        return

    try:
        if is_leap_year(year):
            print(f"✓ {year} is a leap year.")
            # Additional information
            if year % 100 == 0:
                print(f"  (Century year divisible by 400)")
        else:
            print(f"✗ {year} is not a leap year.")
            # Show next leap year
            next_leap = year + 1
            while not is_leap_year(next_leap):
                next_leap += 1
            print(f"  (Next leap year: {next_leap})")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
