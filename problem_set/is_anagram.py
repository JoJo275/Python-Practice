"""is_anagram.py

2) is_anagram(s1, s2)
- Description: Return True if `s1` and `s2` are anagrams
(case-insensitive, ignore spaces and punctuation), otherwise False.
- Input: two strings
- Output: boolean

"""

# !/usr/bin/env python3


def _normalize(s: str) -> str:
    """Normalize a string for anagram comparison.

    Converts to lowercase and removes all non-alphanumeric characters.

    Args:
        s: The string to normalize.

    Returns:
        A lowercase string containing only letters and numbers.

    Example:
        >>> _normalize("Listen!")
        'listen'
        >>> _normalize("A gentleman")
        'agentleman'
    """
    s = s.lower()
    return ''.join(ch for ch in s if ch.isalnum())


def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams of each other.

    Two strings are anagrams if they contain the same characters in the same
    quantities, ignoring case, spaces, and punctuation.

    Args:
        s1: The first string to compare.
        s2: The second string to compare.

    Returns:
        True if s1 and s2 are anagrams, False otherwise.

    Examples:
        >>> is_anagram("Listen", "Silent")
        True
        >>> is_anagram("A gentleman", "Elegant man")
        True
        >>> is_anagram("Hello", "World")
        False
    """
    a = _normalize(s1)
    b = _normalize(s2)
    return sorted(a) == sorted(b)


def main() -> None:
    """Main function to demonstrate is_anagram usage."""
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    result = is_anagram(str1, str2)
    print(f"'{str1}' and '{str2}' are anagrams: {result}")


if __name__ == "__main__":
    main()
