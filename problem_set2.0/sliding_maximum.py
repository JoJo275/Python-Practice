#!/usr/bin/env python3
"""
Sliding Window Maximum

Problem: Given a list of numbers and a window size k, return the maximum
         value in each window as it slides from left to right.

Example: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
         Window [1, 3, -1]    → max = 3
         Window [3, -1, -3]   → max = 3
         Window [-1, -3, 5]   → max = 5
         Window [-3, 5, 3]    → max = 5
         Window [5, 3, 6]     → max = 6
         Window [3, 6, 7]     → max = 7
         Answer: [3, 3, 5, 5, 6, 7]

Approach: Use a deque (double-ended queue) to track indices of useful
          elements. Keep it in decreasing order so max is always at front.
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Find the maximum value in each sliding window of size k.

    Args:
        nums: A list of integers
        k: The window size

    Returns:
        A list of maximum values for each window position

    Examples:
        >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
        >>> max_sliding_window([1], 1)
        [1]
    """
    # Edge case
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # Stores INDICES (not values), in decreasing order

    for i in range(len(nums)):
        # Remove indices outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they'll never be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Add max to result once we have a full window
        if i >= k - 1:
            result.append(nums[dq[0]])  # Front is always the max

    return result


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test case
    numbers = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Input: {numbers}, k={k}")
    print(f"Max in each window: {max_sliding_window(numbers, k)}")
    # Output: [3, 3, 5, 5, 6, 7]
