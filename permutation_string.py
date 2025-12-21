# !/usr/bin/env python3
"""permutation_string.py - Permutation in String Solution

Problem Statement:
------------------
Given two strings s1 and s2, return True if s2 contains a permutation of s1.
In other words, check if any anagram of s1 exists as a substring in s2.

What is a Permutation?
----------------------
A permutation is a rearrangement of letters. Same letters, different order.

Examples:
    - "ab" permutations: "ab", "ba"
    - "abc" permutations: "abc", "acb", "bac", "bca", "cab", "cba"

What Are We Looking For?
------------------------
Does s2 contain ANY window of characters that is a permutation of s1?

Example:
    s1 = "ab", s2 = "eidbaooo"

    Check each window of length 2 in s2:
    - "ei" -> {e:1, i:1} != {a:1, b:1} ❌
    - "id" -> {i:1, d:1} != {a:1, b:1} ❌
    - "db" -> {d:1, b:1} != {a:1, b:1} ❌
    - "ba" -> {b:1, a:1} == {a:1, b:1} ✓ FOUND!

    Return True

Algorithm: Sliding Window with Character Count
----------------------------------------------
1. Count characters in s1 (this is our "target")
2. Slide a window of size len(s1) across s2
3. Count characters in current window
4. If window count == target count, we found a permutation!

Why Sliding Window?
    - We only need to check windows the SAME SIZE as s1
    - As we slide, we add one char and remove one char (efficient!)

Time Complexity: O(n)
    - n = length of s2
    - We visit each character at most twice (enter/exit window)

Space Complexity: O(1)
    - Counter size limited to 26 letters (constant)

Example Input/Output:
--------------------
Input:  s1 = "ab", s2 = "eidbaooo"
Output: True (s2 contains "ba" which is a permutation of "ab")

Input:  s1 = "ab", s2 = "eidboaoo"
Output: False (no permutation of "ab" found)

Usage:
------
    >>> check_inclusion("ab", "eidbaooo")
    True
    >>> check_inclusion("ab", "eidboaoo")
    False
"""

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    """
    Check if any permutation of s1 exists as a substring in s2.

    Args:
        s1: Pattern string to find permutation of.
        s2: String to search within.

    Returns:
        True if s2 contains a permutation of s1, False otherwise.
    """
    if len(s1) > len(s2):
        return False

    # Count characters in s1 (our target)
    s1_count = Counter(s1)
    # Count characters in first window of s2
    window_count = Counter(s2[:len(s1)])

    # Check first window
    if s1_count == window_count:
        return True

    # Slide window across s2
    for i in range(len(s1), len(s2)):
        # Add new character (entering window)
        window_count[s2[i]] += 1
        # Remove old character (leaving window)
        old_char = s2[i - len(s1)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]  # Remove zero counts for clean comparison

        # Check if current window matches
        if s1_count == window_count:
            return True

    return False


if __name__ == "__main__":
    # Get user input
    s1 = input("Enter pattern string (s1): ")
    s2 = input("Enter string to search in (s2): ")

    if s1 and s2:
        result = check_inclusion(s1, s2)
        print(f"\nDoes '{s2}' contain a permutation of '{s1}'? {result}")
    else:
        print("Please enter both strings.")
