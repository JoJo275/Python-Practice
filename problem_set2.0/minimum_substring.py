#!/usr/bin/env python3
"""
Minimum Window Substring

Problem: Given two strings s and t, find the smallest substring of s
         that contains ALL characters from t (including duplicates).

Example: s = "ADOBECODEBANC", t = "ABC" → Answer is "BANC"
         Because "BANC" contains A, B, and C in just 4 characters.

Approach: Use a sliding window. Expand right until we have all chars,
          then shrink left to find the smallest valid window.
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring containing all characters of t.

    Args:
        s: The string to search in
        t: The characters we need to find

    Returns:
        The smallest substring containing all chars of t, or "" if none

    Examples:
        >>> min_window("ADOBECODEBANC", "ABC")
        'BANC'
        >>> min_window("a", "aa")
        ''
    """
    # Edge case: impossible if t is longer
    if len(t) > len(s):
        return ""

    # Count characters we need
    need = Counter(t)
    have = {}  # Characters we have in current window

    need_count = len(need)  # Unique chars needed
    have_count = 0          # Unique chars satisfied

    left = 0
    result = ""
    min_len = float("inf")

    for right in range(len(s)):
        # Add right character to window
        char = s[right]
        have[char] = have.get(char, 0) + 1

        # Check if this char is now satisfied
        if char in need and have[char] == need[char]:
            have_count += 1

        # Shrink window while we have all chars
        while have_count == need_count:
            # Update result if this window is smaller
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                result = s[left:right + 1]

            # Remove left char and shrink
            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                have_count -= 1
            left += 1

    return result


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test case
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"String: '{s}'")
    print(f"Target: '{t}'")
    print(f"Minimum window: '{min_window(s, t)}'")
    # Output: "BANC" (contains A, B, C in just 4 chars)
