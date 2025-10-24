"""num_attributes.py

Ask the user for two numbers and print their sum, difference, product, and
quotient.

This module provides a simple calculator that performs basic arithmetic
operations on two user-provided numbers with proper error handling and
formatted output.
"""

# !/usr/bin/env python3

from typing import Optional, Dict, Any
import math


def calculate_attributes(num1: float, num2: float) -> Dict[str, Any]:
    """Calculate various mathematical attributes of two numbers.

    Performs basic arithmetic operations (sum, difference, product, quotient)
    and additional mathematical calculations on two numbers. All results are
    rounded to 2 decimal places for display purposes.

    Args:
        num1 (float): The first number for calculations.
        num2 (float): The second number for calculations.

    Returns:
        Dict[str, Any]: A dictionary containing the following keys:
            - 'sum': The sum of num1 and num2
            - 'difference': num1 minus num2
            - 'product': The product of num1 and num2
            - 'quotient': num1 divided by num2 (or None if num2 is 0)
            - 'power': num1 raised to the power of num2
            - 'modulo': The remainder of num1 divided by num2 (or None if num2 is 0)
            - 'average': The arithmetic mean of num1 and num2
            - 'maximum': The larger of the two numbers
            - 'minimum': The smaller of the two numbers

    Examples:
        >>> results = calculate_attributes(10, 3)
        >>> results['sum']
        13.0
        >>> results['quotient']
        3.33

        >>> results = calculate_attributes(5, 0)
        >>> results['quotient'] is None
        True

    Note:
        Division by zero returns None instead of raising an exception.
        Very large power operations are handled with overflow protection.
    """
    results = {
        'sum': round(num1 + num2, 2),
        'difference': round(num1 - num2, 2),
        'product': round(num1 * num2, 2),
        'average': round((num1 + num2) / 2, 2),
        'maximum': round(max(num1, num2), 2),
        'minimum': round(min(num1, num2), 2)
    }

    # Handle division by zero
    if num2 != 0:
        results['quotient'] = round(num1 / num2, 2)
        results['modulo'] = round(num1 % num2, 2)
    else:
        results['quotient'] = None
        results['modulo'] = None

    # Handle power operation with overflow protection
    try:
        if abs(num2) < 100:  # Prevent excessive computation
            results['power'] = round(num1 ** num2, 2)
        else:
            results['power'] = "Too large to compute"
    except (OverflowError, ValueError):
        results['power'] = "Cannot compute"

    return results


def format_output(results: Dict[str, Any]) -> None:
    """Format and display calculation results in an aligned table.

    Prints the results dictionary in a nicely formatted, aligned table
    with appropriate handling of None values and special cases.

    Args:
        results (Dict[str, Any]): Dictionary containing calculation results
            from calculate_attributes function.

    Returns:
        None

    Examples:
        >>> results = {'sum': 10.0, 'difference': 4.0, 'quotient': None}
        >>> format_output(results)
        ╔══════════════════════════════════════╗
        ║        Calculation Results           ║
        ╠══════════════════════════════════════╣
        ║ Sum............: 10.00               ║
        ║ Difference.....: 4.00                ║
        ║ Quotient.......: Undefined (÷ by 0)  ║
        ╚══════════════════════════════════════╝
    """
    print("\n╔══════════════════════════════════════╗")
    print("║        Calculation Results           ║")
    print("╠══════════════════════════════════════╣")

    for operation, value in results.items():
        operation_display = operation.replace('_', ' ').title()

        if value is None:
            if operation in ['quotient', 'modulo']:
                value_display = "Undefined (÷ by 0)"
            else:
                value_display = "N/A"
        elif isinstance(value, str):
            value_display = value
        else:
            value_display = f"{value:.2f}"

        print(f"║ {operation_display:.<15}: {value_display:<20} ║")

    print("╚══════════════════════════════════════╝")


def get_valid_number(prompt: str, attempt: int = 1, max_attempts: int = 3) -> Optional[float]:
    """Get a valid number from user input with error handling and retry logic.

    Prompts the user for a number and validates the input. Allows multiple
    attempts if invalid input is provided.

    Args:
        prompt (str): The prompt message to display to the user.
        attempt (int, optional): Current attempt number. Defaults to 1.
        max_attempts (int, optional): Maximum number of attempts allowed.
            Defaults to 3.

    Returns:
        Optional[float]: The validated number if successful, None if all
            attempts are exhausted.

    Raises:
        No exceptions are raised; all errors are handled internally.

    Examples:
        >>> # User enters "10.5"
        >>> num = get_valid_number("Enter a number: ")
        >>> num
        10.5

        >>> # User enters "abc" three times
        >>> num = get_valid_number("Enter a number: ")
        >>> num is None
        True

    Note:
        The function provides helpful error messages and shows remaining
        attempts when invalid input is detected.
    """
    try:
        value = float(input(prompt))

        # Check for special values
        if math.isnan(value):
            print("Error: NaN (Not a Number) is not a valid input.")
            raise ValueError
        if math.isinf(value):
            print("Error: Infinity is not a valid input.")
            raise ValueError

        return value

    except ValueError:
        remaining = max_attempts - attempt

        if remaining > 0:
            print(f"Invalid input. Please enter a valid number. "
                  f"({remaining} attempt{'s' if remaining > 1 else ''} remaining)")
            return get_valid_number(prompt, attempt + 1, max_attempts)
        else:
            print("Maximum attempts exceeded. Exiting...")
            return None
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return None


def main() -> None:
    """Main function to orchestrate user interaction and calculations.

    Manages the main program flow including:
    - Welcome message
    - Getting user input with validation
    - Performing calculations
    - Displaying results
    - Offering to continue with new calculations

    Returns:
        None

    Note:
        The function runs in a loop allowing multiple calculations until
        the user chooses to exit.
    """
    print("╔════════════════════════════════════════╗")
    print("║   Welcome to the Number Calculator     ║")
    print("╚════════════════════════════════════════╝")

    while True:
        print("\n" + "=" * 42)

        # Get first number
        num1 = get_valid_number("Enter the first number: ")
        if num1 is None:
            break

        # Get second number
        num2 = get_valid_number("Enter the second number: ")
        if num2 is None:
            break

        # Perform calculations
        print(f"\nCalculating attributes for {num1:.2f} and {num2:.2f}...")
        results = calculate_attributes(num1, num2)

        # Display results
        format_output(results)

        # Ask if user wants to continue
        print("\n" + "=" * 42)
        while True:
            continue_choice = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")

        if continue_choice in ['no', 'n']:
            print("\nThank you for using the Number Calculator!")
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please report this issue if it persists.")
