"""greeting.py

Write a program that asks for your name and age, then prints a greeting.

"""

# !/usr/bin/env python3


def greet_user() -> None:
    """Ask for user's name and age, then print a greeting."""
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f"Hello, {name}! You are {age} years old.")


def main() -> None:
    """Main function to run the greeting program."""
    greet_user()


if __name__ == "__main__":
    main()
