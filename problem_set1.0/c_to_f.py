"""c_to_f.py

Convert a temperature from Celsius to Fahrenheit.

This module provides a simple command-line interface for converting
temperatures from Celsius to Fahrenheit. The program runs in a continuous
loop, allowing multiple conversions until the user chooses to exit.

Features:
    - Continuous conversion loop
    - Input validation and error handling
    - User-friendly interface with clear instructions
    - Multiple exit commands (quit, exit, q)
    - Rounded output to 2 decimal places

Usage:
    Run the script directly from the command line:
    $ python c_to_f.py
    
Author: Your Name
Date: Current Date
Version: 1.0
"""

# !/usr/bin/env python3

# Import statements would go here if needed
# Currently, only using Python built-in functions


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit.

    Uses the formula: F = (C × 9/5) + 32
    where F is Fahrenheit and C is Celsius.

    Args:
        celsius (float): Temperature in degrees Celsius.
                        Can be positive, negative, or zero.

    Returns:
        float: Temperature in degrees Fahrenheit, rounded to 2 decimal places.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
        >>> celsius_to_fahrenheit(37)  # Normal body temperature
        98.6
        
    Note:
        The function rounds the result to 2 decimal places for better
        readability and practical use.
    """
    # Apply the conversion formula: multiply by 9/5 and add 32
    fahrenheit = (celsius * 9/5) + 32
    
    # Round to 2 decimal places for cleaner output
    return round(fahrenheit, 2)


def main() -> None:
    """Main function to run the temperature converter program.
    
    This function provides a command-line interface for the temperature
    converter. It runs in a continuous loop, prompting the user for
    Celsius temperatures and displaying the Fahrenheit equivalent.
    
    The loop continues until the user enters one of the exit commands:
    'quit', 'exit', or 'q' (case-insensitive).
    
    Features:
        - Input validation with helpful error messages
        - Graceful handling of invalid inputs
        - Clear user instructions
        - Multiple exit command options
    
    Returns:
        None
        
    Raises:
        No exceptions are raised; all errors are handled internally
        with user-friendly messages.
    """
    # Display welcome message and program header
    print("=== Celsius to Fahrenheit Converter ===")
    print("Type 'quit', 'exit', or 'q' to stop the program.\n")

    # Main program loop - continues until user chooses to exit
    while True:
        # Get user input and remove leading/trailing whitespace
        user_input: str = input("Enter temperature in Celsius: ").strip()

        # Check if user wants to quit the program
        # Convert to lowercase for case-insensitive comparison
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the temperature converter. Goodbye!")
            break  # Exit the while loop and end the program

        # Try to convert input to float and perform conversion
        try:
            # Attempt to parse the user input as a floating-point number
            celsius: float = float(user_input)
            
            # Perform the temperature conversion
            fahrenheit: float = celsius_to_fahrenheit(celsius)
            
            # Display the result with proper formatting
            # Using degree symbols (°) for better readability
            print(f"{celsius}°C is equal to {fahrenheit}°F\n")
            
        except ValueError:
            # Handle case where input cannot be converted to a number
            # This catches inputs like "abc", "12.34.56", empty strings, etc.
            print(f"Error: '{user_input}' is not a valid number. Please enter a numeric value.\n")
            
        except Exception as e:
            # Catch-all for any unexpected errors
            # This ensures the program doesn't crash unexpectedly
            print(f"An unexpected error occurred: {e}\n")


# Standard Python idiom to check if script is run directly (not imported)
if __name__ == "__main__":
    # Only execute main() if this script is run directly
    # This allows the module to be imported without running the CLI
    main()
