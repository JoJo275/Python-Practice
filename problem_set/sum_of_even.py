"""sum_of_even.py

1) sum_of_even(n)
- Description: Return the sum of all even numbers from 1 to n (inclusive). If
n < 1 return 0.
- Input: integer n >= any int
- Output: integer

"""


def sum_of_even(n: int) -> int:
    """Return the sum of all even numbers from 1 to n (inclusive).

    If n < 1, return 0.

    Args:
        n: An integer value (inclusive upper bound).

    Returns:
        The sum of all even numbers from 1 to n (inclusive).
    """
    if n < 1:
        return 0
    return sum(i for i in range(1, n + 1) if i % 2 == 0)


def main():
    """Main function to demonstrate sum_of_even usage."""
    i = int(input("Enter an integer n to compute sum_of_even(n): "))
    print(sum_of_even(i))


if __name__ == "__main__":
    main()
