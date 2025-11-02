#!/usr/bin/env python3
"""

Check if a number is even or odd.

"""

def is_even_or_odd(number):
    """Determine if a number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    result = is_even_or_odd(num)
    print(f"The number {num} is {result}.")
