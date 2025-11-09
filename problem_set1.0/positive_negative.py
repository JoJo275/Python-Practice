#!/usr/bin/env python3
"""positive_negative.py

Check whether a number is positive, negative, or zero.

This module demonstrates basic conditional logic and number classification.
It handles both integer and floating-point numbers.
"""

from typing import Union


def check_number(num: Union[int, float]) -> str:
    """
    Determine if a number is positive, negative, or zero.

    Args:
        num: A numeric value (int or float) to check

    Returns:
        A string indicating whether the number is "Positive", "Negative", or "Zero"

    Examples:
        >>> check_number(5)
        'Positive'
        >>> check_number(-3.14)
        'Negative'
        >>> check_number(0)
        'Zero'
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def main() -> None:
    """Main function to run the number checker program."""
    try:
        # Get user input and convert to float
        number = float(input("Enter a number: "))

        # Check the number
        result = check_number(number)

        # Display result with additional information
        print(f"The number {number} is {result}.")

        # Add absolute value information for educational purposes
        if number != 0:
            print(f"Its absolute value is {abs(number)}.")

    except ValueError:
        print("Error: Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")


if __name__ == "__main__":
    main()
