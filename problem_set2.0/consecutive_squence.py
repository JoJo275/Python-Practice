#!/usr/bin/env python3
"""
Longest Consecutive Sequence

Problem: Given a list of numbers, find the length of the longest
         sequence of consecutive numbers.

Example: [100, 4, 200, 1, 3, 2] → Answer is 4
         Because [1, 2, 3, 4] is the longest consecutive sequence.

Approach: Use a set for O(1) lookups. For each number, check if it's
          the START of a sequence (no num-1 exists), then count up.
"""


def longest_consecutive(nums: list[int]) -> int:
    """
    Find the longest consecutive sequence in a list of numbers.

    Args:
        nums: A list of integers (can be unsorted, may have duplicates)

    Returns:
        The length of the longest consecutive sequence

    Examples:
        >>> longest_consecutive([100, 4, 200, 1, 3, 2])
        4
        >>> longest_consecutive([0, 0])
        1
    """
    # Edge case: empty list has no sequence
    if not nums:
        return 0

    # Convert to set (removes duplicates, enables fast lookup)
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if this is the START of a sequence
        # (meaning num-1 is NOT in the set)
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Count consecutive numbers going up
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update longest if we found a longer sequence
            longest = max(longest, current_length)

    return longest


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test cases
    test1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {test1}")
    print(f"Longest consecutive sequence: {longest_consecutive(test1)}")
    # Output: 4 (the sequence is 1, 2, 3, 4)
