"""

Determine if a year is a leap year.

"""


def is_leap_year(year: int) -> bool:
    """
    Determine if the given year is a leap year.

    A year is a leap year if it is divisible by 4,
    except for end-of-century years, which must be divisible by 400.

    Args:
        year (int): The year to check.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    Examples:
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2021)
        False
    """

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    user = int(input("Enter a year: "))
    if is_leap_year(user):
        print(f"{user} is a leap year.")
    else:
        print(f"{user} is not a leap year.")
