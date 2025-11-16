#!/usr/bin/env python3
"""two_sum.py

Arrays & Hashing (Easy)

Two Sum:
Given an array and a target, find indices of two numbers that add up to the
target (exactly one solution, no reuse of elements).

"""

from typing import List, Optional, Tuple
def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find indices of the two numbers in `nums` that add up to `target`.

    This function uses a hash map to store the numbers and their indices
    as we iterate through the list. For each number, we check if the
    complement (target - current number) exists in the map.

    Args:
        nums: List of integers to search through.
        target: The target sum we are looking for.
    Returns:
        A tuple of the two indices if a solution is found, None otherwise.
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([3, 3], 6)
        (0, 1)
    """

    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], index)
        num_to_index[num] = index
    return None

if __name__ == "__main__":
    # Example usage
    example_nums = [2, 7, 11, 15]
    example_target = 9
    result = two_sum(example_nums, example_target)
    if result:
        print(f"Indices of numbers that add up to {example_target}: {result}")
    else:
        print("No two numbers add up to the target.")
            continue

            year = int(user_input)
            if year <= 0:
                print("Please enter a positive integer for the year.")
                continue

            return year
        except ValueError:
            print("Invalid input. Please enter a valid year or 'quit' to exit.")
            print(f"Stored password retrieved successfully.")
    if verify_password(stored_password, debug_mode):
        print("Access granted")
    else:
        print("Access denied")

