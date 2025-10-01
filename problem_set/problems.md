Problem Set: Python Practice

This set contains 6 problems of increasing difficulty. Solve each problem by implementing the required functions in `solutions.py` and run the tests in `tests/`.

Problems

1) sum_of_even(n)
- Description: Return the sum of all even numbers from 1 to n (inclusive). If n < 1 return 0.
- Input: integer n >= any int
- Output: integer

2) is_anagram(s1, s2)
- Description: Return True if `s1` and `s2` are anagrams (case-insensitive, ignore spaces and punctuation), otherwise False.
- Input: two strings
- Output: boolean

3) fibonacci(n)
- Description: Return the nth Fibonacci number, with fibonacci(0)=0, fibonacci(1)=1. For n<0 raise ValueError.
- Input: integer n
- Output: integer

4) flatten(lst)
- Description: Given a list which can contain nested lists to arbitrary depth, return a flattened list with all elements in order.
- Input: list (elements can be lists)
- Output: list

5) group_by_key(items, key)
- Description: Given a list of dicts `items` and a `key` string, return a dict mapping key values to lists of items with that key. If an item doesn't have the key, group under None.
- Input: list of dicts, string key
- Output: dict

6) shortest_path(grid)
- Description: Given a 2D grid (list of lists) with 0 for open cell and 1 for wall, return the length of shortest path from top-left (0,0) to bottom-right (m-1,n-1) moving 4-directionally. If no path, return -1. Grid is non-empty.
- Input: list[list[int]]
- Output: integer

Notes
- Implementations should be in `solutions.py`.
- Tests are provided in `tests/test_problems.py`.
- Keep functions pure and include docstrings.
