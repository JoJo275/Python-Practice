""" fibonacci.py

3) fibonacci(n)
- Description: Return the nth Fibonacci number, with fibonacci(0)=0, fibonacci(1)=1. For n<0 raise ValueError.
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



def main():


if __name__ == "__main__":
    main()
