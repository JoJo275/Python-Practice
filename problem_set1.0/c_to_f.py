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

user_input = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(user_input)
    print(f"{user_input}°C is equal to {fahrenheit}°F")

if __name__ == "__main__":
    main()
