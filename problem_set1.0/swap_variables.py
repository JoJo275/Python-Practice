#!/usr/bin/env python3
"""swap_variables.py

Module for demonstrating variable swapping in Python.

This module showcases Python's tuple unpacking feature to swap two variables
without using a temporary third variable. This is a Pythonic approach that
leverages the language's ability to perform simultaneous assignments.

The traditional approach in other languages would require:
    temp = a
    a = b
    b = temp

Python's approach:
    a, b = b, a

Author: [Your Name]
Date: [Current Date]
Python Version: 3.x
"""


def main() -> None:
    """
    Main function to swap two variables and display the result.

    This function demonstrates the Pythonic way of swapping variables
    using tuple unpacking. It prompts the user for two values,
    displays them before swapping, performs the swap operation,
    and then displays the swapped values.

    Returns:
        None: This function doesn't return any value, it only prints output.

    Example:
        >>> main()
        Enter the value of variable a: 10
        Enter the value of variable b: 20
        Before swapping: a = 10, b = 20
        After swapping: a = 20, b = 10

    Note:
        - Input values are treated as strings
        - No type conversion is performed
        - Works with any data type that can be entered as string
    """
    # Prompt user for the first variable value
    # Note: input() always returns a string in Python 3
    a: str = input("Enter the value of variable a: ")

    # Prompt user for the second variable value
    b: str = input("Enter the value of variable b: ")

    # Display the original values before swapping
    print(f"Before swapping: a = {a}, b = {b}")

    # Perform the swap using Python's tuple unpacking
    # Behind the scenes: Python creates a tuple (b, a) on the right side,
    # then unpacks it to assign b's value to a and a's value to b simultaneously
    a, b = b, a

    # Display the values after swapping to demonstrate the result
    print(f"After swapping: a = {a}, b = {b}")


# Script entry point - ensures main() only runs when script is executed directly
# and not when imported as a module
if __name__ == "__main__":
    main()
