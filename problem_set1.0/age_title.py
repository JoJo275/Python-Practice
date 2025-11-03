#!/usr/bin/env python3
"""age_title.py

Educational module for age classification.

This module demonstrates:
- Input validation and error handling
- Type hints for better code documentation
- Conditional logic with if/elif/else chains
- String formatting techniques
- Function documentation with docstrings

Age Categories:
    - Child (0-12): Elementary school age
    - Teenager (13-17): Secondary school age
    - Adult (18-64): Working age
    - Senior (65+): Retirement age

Author: [Your Name]
Date: [Current Date]
Python Version: 3.6+
"""

from typing import Optional


def get_age_title(age: int) -> str:
    """
    Classify a person's age into a category.

    This function uses conditional statements to determine
    which age category a person belongs to based on their age.

    Args:
        age: The person's age in years (must be non-negative)

    Returns:
        A string describing the age category

    Raises:
        ValueError: If age is negative

    Examples:
        >>> get_age_title(5)
        'child'
        >>> get_age_title(15)
        'teenager'
        >>> get_age_title(25)
        'adult'
        >>> get_age_title(70)
        'senior'
    """
    # Validate input - ages cannot be negative
    if age < 0:
        raise ValueError("Age cannot be negative")

    # Check age ranges using elif chain
    # The order matters - we check from youngest to oldest
    if age < 13:
        return "child"
    elif age < 18:
        return "teenager"
    elif age < 65:
        return "adult"
    else:  # age >= 65
        return "senior"


def get_age_description(age: int) -> str:
    """
    Get a detailed description for an age category.

    Args:
        age: The person's age in years

    Returns:
        A detailed description of the age category
    """
    title = get_age_title(age)

    # Dictionary mapping titles to descriptions
    # This demonstrates the dictionary data structure
    descriptions = {
        "child": "You are in your childhood years, a time of learning and growth.",
        "teenager": "You are a teenager, experiencing the transition to adulthood.",
        "adult": "You are an adult with full legal rights and responsibilities.",
        "senior": "You are a senior citizen with a lifetime of experience.",
    }

    return descriptions.get(title, "Unknown age category")


def get_valid_age() -> Optional[int]:
    """
    Get a valid age from user input with error handling.

    This function demonstrates:
    - Input validation
    - Exception handling
    - User-friendly error messages

    Returns:
        Valid age as integer, or None if user wants to quit
    """
    while True:
        try:
            # Get user input
            user_input = input("Enter your age (or 'quit' to exit): ").strip()

            # Check for exit command
            if user_input.lower() == "quit":
                return None

            # Try to convert to integer
            age = int(user_input)

            # Validate the age range
            if age < 0:
                print("❌ Age cannot be negative. Please try again.")
                continue
            elif age > 150:
                print("❌ That age seems unrealistic. Please enter a valid age.")
                continue

            return age

        except ValueError:
            # Handle non-numeric input
            print(f"❌ '{user_input}' is not a valid number. Please enter a numeric age.")


def main() -> None:
    """
    Main function to run the age classification program.

    This demonstrates a complete program flow with:
    - User interaction
    - Input validation
    - Output formatting
    """
    print("=" * 50)
    print("AGE CLASSIFICATION PROGRAM")
    print("=" * 50)
    print(
        "\nThis program will classify your age into a category."
        "\nAge categories: Child (0-12), Teenager (13-17), Adult (18-64), Senior (65+)\n"
    )

    # Get valid age from user
    age = get_valid_age()

    if age is None:
        print("Goodbye!")
        return

    # Get classification
    title = get_age_title(age)
    description = get_age_description(age)

    # Display results with formatting
    print("\n" + "=" * 50)
    print(f"Age: {age} years old")
    print(f"Classification: You are a {title}.")
    print(f"Description: {description}")
    print("=" * 50)

    # Additional educational information
    if age < 18:
        years_to_adult = 18 - age
        print(
            f"\n📚 Educational Note: You will be an adult in {years_to_adult} "
            f"year{'s' if years_to_adult != 1 else ''}."
        )
    elif age < 65:
        years_to_senior = 65 - age
        print(
            f"\n📚 Educational Note: You will be a senior in {years_to_senior} "
            f"year{'s' if years_to_senior != 1 else ''}."
        )


if __name__ == "__main__":
    # This block only runs when the script is executed directly,
    # not when imported as a module
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
