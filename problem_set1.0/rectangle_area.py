"""rectangle_area.py

Find the area of a rectangle using user input for width and height.

This module provides a command-line interface for calculating the area
of rectangles. Users can input width and height values, and the program
will compute and display the area. The program includes input validation,
error handling, and the option to perform multiple calculations.

Features:
    - Calculate rectangle area using the formula: area = width × height
    - Input validation for positive numeric values
    - Continuous calculation loop with exit options
    - Detailed error messages for invalid inputs
    - Support for decimal values
    - Formatted output with units

Usage:
    Run the script directly from the command line:
    $ python rectangle_area.py

    Then follow the prompts to enter width and height values.

Examples:
    >>> Enter the width of the rectangle: 5.5
    >>> Enter the height of the rectangle: 3.2
    >>> The area of the rectangle is: 17.6 square units

Author: Your Name
Date: Current Date
Version: 2.0

Notes:
    - Both width and height must be positive numbers
    - The program accepts both integer and decimal values
    - Results are rounded to 2 decimal places for readability
"""

# !/usr/bin/env python3

# Import statements for type hints
from typing import Optional


def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle.

    Uses the formula: Area = width × height

    Args:
        width (float): The width of the rectangle. Must be positive.
        height (float): The height of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle, rounded to 2 decimal places.

    Raises:
        ValueError: If width or height is negative or zero.

    Examples:
        >>> calculate_rectangle_area(5, 3)
        15.0
        >>> calculate_rectangle_area(4.5, 2.2)
        9.9
        >>> calculate_rectangle_area(10, 10)
        100.0

    Note:
        The function rounds the result to 2 decimal places to avoid
        floating-point precision issues in display.
    """
    # Validate that dimensions are positive
    if width <= 0:
        raise ValueError(f"Width must be positive, got {width}")
    if height <= 0:
        raise ValueError(f"Height must be positive, got {height}")

    # Calculate area using the rectangle area formula
    area = width * height

    # Round to 2 decimal places for cleaner output
    return round(area, 2)


def get_positive_float(prompt: str) -> Optional[float]:
    """Get a positive float value from user input.

    Continuously prompts the user until a valid positive number is entered
    or the user chooses to quit.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        Optional[float]: The positive float value entered by the user,
                        or None if the user chose to quit.

    Note:
        Accepts 'quit', 'exit', or 'q' to return None.
        Only accepts positive numbers (greater than 0).
    """
    while True:
        # Get user input and strip whitespace
        user_input = input(prompt).strip()

        # Check for quit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            return None

        try:
            # Attempt to convert input to float
            value = float(user_input)

            # Validate that the value is positive
            if value <= 0:
                print(f"Error: Value must be positive. You entered {value}.")
                print("Please enter a positive number greater than 0.\n")
                continue

            # Return valid positive value
            return value

        except ValueError:
            # Handle non-numeric input
            print(f"Error: '{user_input}' is not a valid number.")
            print("Please enter a numeric value (e.g., 5, 3.14).\n")
        except Exception as e:
            # Handle any unexpected errors
            print(f"Unexpected error: {e}")
            print("Please try again.\n")


def main() -> None:
    """Main function to calculate the area of a rectangle.

    This function provides a user-friendly command-line interface for
    calculating rectangle areas. It runs in a continuous loop, allowing
    users to calculate multiple rectangle areas until they choose to exit.

    Features:
        - Continuous calculation loop
        - Input validation for positive numbers only
        - Clear error messages for invalid inputs
        - Option to quit at any input prompt
        - Formatted output with proper units
        - Summary of calculations performed

    The function handles all user interaction, including:
        - Displaying welcome messages and instructions
        - Collecting width and height inputs
        - Performing calculations
        - Displaying results
        - Offering to continue or exit

    Returns:
        None
    Raises:
        - ValueError: If width or height is not positive
        - Exception: For unexpected issues during input or calculation
    Side Effects:
        - Prints to console (stdout)
        - Reads from console (stdin)
    """
    # Display welcome message and program information
    print("=" * 50)
    print("     RECTANGLE AREA CALCULATOR")
    print("=" * 50)
    print("\nThis program calculates the area of a rectangle.")
    print("Enter 'quit', 'exit', or 'q' at any prompt to stop.\n")

    # Counter for number of calculations performed
    calculation_count = 0

    # Main program loop - continues until user chooses to exit
    while True:
        print(f"\n--- Calculation #{calculation_count + 1} ---")

        # Get width from user with validation
        print("Step 1: Enter the width")
        width = get_positive_float("Width of the rectangle: ")

        # Check if user wants to quit
        if width is None:
            print("\nExiting calculator...")
            break

        # Get height from user with validation
        print("\nStep 2: Enter the height")
        height = get_positive_float("Height of the rectangle: ")

        # Check if user wants to quit
        if height is None:
            print("\nExiting calculator...")
            break

        try:
            # Calculate the area using the dedicated function
            area = calculate_rectangle_area(width, height)

            # Display the results with formatting
            print("\n" + "=" * 40)
            print("CALCULATION RESULTS:")
            print(f"  Width:  {width} units")
            print(f"  Height: {height} units")
            print(f"  Area:   {area} square units")
            print("=" * 40)

            # Increment successful calculation counter
            calculation_count += 1

            # Ask if user wants to perform another calculation
            print("\nWould you like to calculate another rectangle?")
            continue_choice = input("Enter 'yes' to continue or any other key to exit: ").strip().lower()

            # Check if user wants to continue
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using the Rectangle Area Calculator!")
                break

        except ValueError as e:
            # Handle validation errors from calculate_rectangle_area
            print(f"\nError in calculation: {e}")
            print("Please try again with valid positive values.")

        except Exception as e:
            # Catch-all for any unexpected errors during calculation
            print(f"\nAn unexpected error occurred during calculation: {e}")
            print("Please try again.")

    # Display session summary before exiting
    if calculation_count > 0:
        print(f"\nYou performed {calculation_count} calculation(s) this session.")
    print("Goodbye!\n")


# Standard Python idiom to check if script is run directly
if __name__ == "__main__":
    # Only execute main() if this script is run directly
    # This allows the module to be imported without running the CLI
    main()
