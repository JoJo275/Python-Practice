# !/usr/bin/env python3
"""

Ask the user for their age and print whether they are a minor, adult, or
senior.

"""


def get_age_title(age):
    if age < 18:
        return "minor"
    elif age < 65:
        return "adult"
    else:
        return "senior"


if __name__ == "__main__":
    age = int(input("Enter your age: "))
    title = get_age_title(age)
    print(f"You are classified as a {title}.")
