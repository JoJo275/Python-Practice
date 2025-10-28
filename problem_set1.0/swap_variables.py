"""swap_variables.py

Swap two variables without using a third variable.

"""

# !/usr/bin/env python3


def main():
    """Main function to swap two variables and display the result."""
    # Prompt user for input
    a = input("Enter the value of variable a: ")
    b = input("Enter the value of variable b: ")

    print(f"Before swapping: a = {a}, b = {b}")

    # Swap values without using a third variable
    a, b = b, a

    print(f"After swapping: a = {a}, b = {b}")

if __name__ == "__main__":
    main()
