#! /usr/bin/env python3
"""product_of_array_except_self.py - Product of Array Except Self Solution

Problem Statement:
------------------
Given an array of integers, return an array where each element is the product
of ALL other elements EXCEPT itself (without using division).

What Does This Mean?
--------------------
For each position, multiply every number in the array EXCEPT the one at that position.

Example:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
    
    Breakdown:
    - Index 0: 2 × 3 × 4 = 24  (skip the 1)
    - Index 1: 1 × 3 × 4 = 12  (skip the 2)
    - Index 2: 1 × 2 × 4 = 8   (skip the 3)
    - Index 3: 1 × 2 × 3 = 6   (skip the 4)

Algorithm Explanation (Prefix & Suffix Products):
-------------------------------------------------
Instead of multiplying everything except one element each time (slow!),
we use a clever trick with "prefix" and "suffix" products:

1. PREFIX = product of all numbers BEFORE current index
   [1, 2, 3, 4] -> prefix = [1, 1, 2, 6]
   - Index 0: nothing before -> 1
   - Index 1: 1 -> 1
   - Index 2: 1 × 2 -> 2
   - Index 3: 1 × 2 × 3 -> 6

2. SUFFIX = product of all numbers AFTER current index
   [1, 2, 3, 4] -> suffix = [24, 12, 4, 1]
   - Index 0: 2 × 3 × 4 -> 24
   - Index 1: 3 × 4 -> 12
   - Index 2: 4 -> 4
   - Index 3: nothing after -> 1

3. RESULT = prefix × suffix at each index
   [1×24, 1×12, 2×4, 6×1] = [24, 12, 8, 6] ✓

Time Complexity: O(n)
    - Two passes through the array

Space Complexity: O(n)
    - Storing the result array

Example Input/Output:
--------------------
Input:  [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input:  [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Usage:
------
    >>> product_except_self([1, 2, 3, 4])
    [24, 12, 8, 6]
"""

from math import prod


def product_except_self(nums: list[int]) -> list[int]:
    """
    Calculate product of all elements except self for each position.

    Args:
        nums: List of integers.

    Returns:
        List where each element is product of all others except itself.
    """
    n = len(nums)
    result = [1] * n  # Start with all 1s
    
    # Build prefix products (left to right)
    prefix = 1
    for i in range(n):
        result[i] = prefix       # Store product of all elements before i
        prefix *= nums[i]        # Update prefix to include current element

    # Multiply by suffix products (right to left)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix      # Multiply by product of all elements after i
        suffix *= nums[i]        # Update suffix to include current element

    return result


if __name__ == "__main__":
    # Get user input
    user_input = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")

    # Parse input: split, strip, convert to int
    nums = [int(n.strip()) for n in user_input.split(",") if n.strip()]

    if nums:
        result = product_except_self(nums)
        print(f"\nProduct except self: {result}")
    else:
        print("No numbers entered.")
