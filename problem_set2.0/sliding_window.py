#!/usr/bin/env python3
"""
Sliding Window - Maximum Sum of K Consecutive Elements

Problem: Given a list of numbers and a window size k,
         find the maximum sum of any k consecutive elements.

Example: [1, 4, 2, 10, 2, 3, 1, 0, 20], k=4 → Answer is 24
         Because [2, 10, 2, 3] = 17... wait, [1, 0, 20] is only 3.
         Actually [10, 2, 3, 1] = 16, [3, 1, 0, 20] = 24 ✓

Approach: Instead of recalculating the sum for each window,
          slide the window by removing the left element and
          adding the new right element. Much faster!
"""


def max_sum_subarray(nums: list[int], k: int) -> int:
    """
    Find the maximum sum of k consecutive elements.

    Args:
        nums: A list of integers
        k: The window size (how many consecutive elements)

    Returns:
        The maximum sum of any k consecutive elements

    Examples:
        >>> max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)
        24
        >>> max_sum_subarray([1, 2, 3], 2)
        5
    """
    # Edge case: not enough elements
    if len(nums) < k:
        return 0

    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window: remove left, add right
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# --- Run only when executed directly ---
if __name__ == "__main__":
    # Test case
    numbers = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(f"Input: {numbers}, k={k}")
    print(f"Max sum of {k} consecutive elements: {max_sum_subarray(numbers, k)}")
    # Output: 24 (the window is [3, 1, 0, 20])
