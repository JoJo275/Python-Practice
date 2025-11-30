#! /usr/bin/env python3
"""group_anagrams.py - Group Anagrams Solution

Problem Statement:
------------------
Given a list of strings, group all anagrams together into sublists.

What is an Anagram?
-------------------
An anagram is a word formed by rearranging the letters of another word,
using all original letters exactly once.

Examples:
    - "eat" and "tea" are anagrams (both use: e, a, t)
    - "listen" and "silent" are anagrams
    - "hello" and "world" are NOT anagrams

Algorithm Explanation:
----------------------
1. For each word, create a "signature" by sorting its letters alphabetically
   - "eat" -> "aet"
   - "tea" -> "aet"  (same signature = anagram!)
   
2. Use a dictionary where:
   - KEY = sorted letter signature (tuple for hashability)
   - VALUE = list of words sharing that signature

3. Return all the grouped lists

Time Complexity: O(n * k log k)
    - n = number of words
    - k = maximum word length (sorting each word)

Space Complexity: O(n * k)
    - Storing all words in dictionary

Example Input/Output:
--------------------
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Usage:
------
    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams from a list of strings.

    Args:
        strs: List of lowercase strings to group.

    Returns:
        List of lists, where each sublist contains anagrams.
    """
    # defaultdict auto-creates empty list for new keys
    groups = defaultdict(list)

    for word in strs:
        # tuple(sorted(word)) creates hashable key: "eat" -> ('a','e','t')
        groups[tuple(sorted(word))].append(word)

    return list(groups.values())
