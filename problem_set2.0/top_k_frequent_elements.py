#! /usr/bin/env python3
"""top_k_frequent_elements.py

Top K Frequent Elements

"""

"""top_k_frequent_elements.py - Top K Frequent Elements Solution

Problem Statement:
------------------
Given a list of numbers and an integer k, return the k most frequent elements.

What Does "Frequent" Mean?
--------------------------
Frequency = how many times a number appears in the list.

Example:
    [1, 1, 1, 2, 2, 3] -> 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
    If k=2, return [1, 2] (the two most frequent)

Algorithm Explanation:
----------------------
1. Count how many times each number appears (using Counter)
   - [1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}

2. Get the k elements with highest counts (using most_common)
   - most_common(2) -> [(1, 3), (2, 2)]

3. Extract just the numbers (not the counts)
   - [1, 2]

Time Complexity: O(n log n)
    - n = length of input list
    - Counting is O(n), sorting for most_common is O(n log n)

Space Complexity: O(n)
    - Storing the frequency counts

Example Input/Output:
--------------------
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

Input:  nums = [1], k = 1
Output: [1]

Usage:
------
    >>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    [1, 2]
"""

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Find the k most frequently occurring elements.

    Args:
        nums: List of integers.
        k: Number of top frequent elements to return.

    Returns:
        List of the k most frequent elements.
    """
    # Counter counts occurrences: [1,1,2] -> Counter({1: 2, 2: 1})
    # most_common(k) returns k items as (element, count) tuples
    # We extract just the elements with a list comprehension
    return [num for num, count in Counter(nums).most_common(k)]


if __name__ == "__main__":
    # Get user input
    user_nums = input("Enter numbers separated by commas (e.g., 1,1,1,2,2,3): ")
    k = int(input("How many top frequent elements? (k): "))

    # Parse input: split, strip, convert to int
    nums = [int(n.strip()) for n in user_nums.split(",") if n.strip()]

    if nums and k > 0:
        result = top_k_frequent(nums, k)
        print(f"\nTop {k} frequent elements: {result}")
    else:
        print("Invalid input.")
