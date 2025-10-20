""" fibonacci.py

3) fibonacci(n)
- Description: Return the nth Fibonacci number, with fibonacci(0)=0,
fibonacci(1)=1. For n<0 raise ValueError.
- Input: integer n
- Output: integer

"""

# !/usr/bin/env python3


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1

    Args:
        n: An integer index in the Fibonacci sequence.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def main() -> None:
    """Main function to demonstrate fibonacci usage with error handling.

    Prompts user for input and displays the corresponding Fibonacci number.
    Handles various error cases including invalid input and negative numbers.
    """
    print("=== Fibonacci Number Calculator ===")
    print("This program calculates the nth Fibonacci number.")
    print("Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...")
    print()

    while True:
        try:
            # Get user input
            prompt = "Enter a non-negative integer n (or 'q' to quit): "
            user_input = input(prompt).strip()

            # Allow user to quit
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("Goodbye!")
                break

            # Try to convert to integer
            n = int(user_input)

            # Calculate fibonacci number
            result = fibonacci(n)

            # Display result
            print(f"✓ fibonacci({n}) = {result}")
            print()

        except ValueError as e:
            # Handle ValueError from fibonacci() or int() conversion
            if "non-negative" in str(e).lower():
                print(f"✗ Error: {e}")
            else:
                print("✗ Error: Invalid input. Please enter a valid integer.")
            print()

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nProgram interrupted by user. Goodbye!")
            break

        except Exception as e:
            # Catch any other unexpected errors
            print(f"✗ An unexpected error occurred: {e}")
            print()


if __name__ == "__main__":
    main()
