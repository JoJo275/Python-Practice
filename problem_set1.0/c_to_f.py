"""c_to_f.py

Convert a temperature from Celsius to Fahrenheit.

"""

# !/usr/bin/env python3


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)


def main():
    print("=== Celsius to Fahrenheit Converter ===")
    print("Type 'quit', 'exit', or 'q' to stop the program.\n")

    while True:
        user_input = input("Enter temperature in Celsius: ").strip()

        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the temperature converter. Goodbye!")
            break

        try:
            celsius = float(user_input)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F\n")
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number. Please enter a numeric value.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()
