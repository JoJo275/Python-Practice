#! /usr/bin/env python3
"""encode_decode.py - Encode and Decode Strings Solution

Problem Statement:
------------------
Design an algorithm to encode a list of strings into a single string,
and decode that single string back into the original list.

Why Is This Tricky?
-------------------
Strings can contain ANY characters, including commas, spaces, or delimiters.
So we can't just use "," to join them - what if a string contains ","?

Example of the Problem:
    ["hello,world", "test"] joined with "," -> "hello,world,test"
    How do we know if it was 2 strings or 3? We don't!

The Solution: Length-Prefix Encoding
------------------------------------
Store each string's LENGTH before the string itself, separated by a delimiter.

Format: {length}#{string}{length}#{string}...

Example:
    ["hello", "world"] -> "5#hello5#world"
    
    Breakdown:
    - "5#hello" = length is 5, then read 5 characters: "hello"
    - "5#world" = length is 5, then read 5 characters: "world"

Why This Works:
    - We know EXACTLY how many characters to read
    - Doesn't matter if string contains "#" or any other character
    - ["a#b", "c"] -> "3#a#b1#c" (we read 3 chars after first #: "a#b")

Algorithm Explanation:
----------------------
ENCODE:
    1. For each string, prepend its length + "#"
    2. Join everything together

DECODE:
    1. Read digits until you hit "#" -> that's the length
    2. Read exactly that many characters -> that's the string
    3. Repeat until end of encoded string

Time Complexity: O(n)
    - n = total characters across all strings

Space Complexity: O(n)
    - Storing the encoded/decoded result

Example Input/Output:
--------------------
Input:  ["hello", "world"]
Encode: "5#hello5#world"
Decode: ["hello", "world"]

Input:  ["we", "say", ":", "yes"]
Encode: "2#we3#say1#:3#yes"
Decode: ["we", "say", ":", "yes"]

Usage:
------
    >>> encode(["hello", "world"])
    '5#hello5#world'
    >>> decode("5#hello5#world")
    ['hello', 'world']
"""


def encode(strs: list[str]) -> str:
    """
    Encode a list of strings into a single string.

    Args:
        strs: List of strings to encode.

    Returns:
        Single encoded string with length prefixes.
    """
    # Format: "length#string" for each string
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s: str) -> list[str]:
    """
    Decode a single string back into a list of strings.

    Args:
        s: Encoded string to decode.

    Returns:
        Original list of strings.
    """
    result = []
    i = 0
    
    while i < len(s):
        # Find the "#" delimiter to get the length
        j = s.index("#", i)          # Find next "#" starting from i
        length = int(s[i:j])          # Characters before "#" = length
        result.append(s[j + 1:j + 1 + length])  # Extract the string
        i = j + 1 + length            # Move to next encoded string
    
    return result


if __name__ == "__main__":
    # Get user input
    user_input = input("Enter strings separated by commas (e.g., hello,world): ")
    
    # Parse input
    strings = [s.strip() for s in user_input.split(",")]
    
    if strings:
        encoded = encode(strings)
        decoded = decode(encoded)
        print(f"\nOriginal:  {strings}")
        print(f"Encoded:   '{encoded}'")
        print(f"Decoded:   {decoded}")
    else:
        print("No strings entered.")
