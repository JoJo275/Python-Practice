#!/usr/bin/env python3
"""
Longest Substring Without Repeating Characters

Problem: Given a string, find the length of the longest substring
         that contains no repeating characters.

Example: "abcabcbb" → Answer is 3
         Because "abc" is the longest substring with all unique chars.

Approach: Use a sliding window with a set to track characters.
          Expand right side, shrink left side when we hit a duplicate.
"""


def longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s: The input string

    Returns:
        The length of the longest substring with all unique characters

    Examples:
        >>> longest_substring("abcabcbb")
        3
        >>> longest_substring("bbbbb")
        1
        >>> longest_substring("pwwkew")
        3
    """
    char_set = set()  # Characters in current window
    left = 0          # Left pointer of window
    max_length = 0    # Longest substring found

    for right in range(len(s)):
        # If char is duplicate, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current char to window
        char_set.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test cases
    test = "abcabcbb"
    print(f"Input: '{test}'")
    print(f"Longest substring length: {longest_substring(test)}")
    # Output: 3 (the substring is "abc")
 