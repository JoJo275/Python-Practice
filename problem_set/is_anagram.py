"""is_anagram.py

2) is_anagram(s1, s2)
- Description: Return True if `s1` and `s2` are anagrams (case-insensitive, ignore spaces and punctuation), otherwise False.
- Input: two strings
- Output: boolean

"""

# !/usr/bin/env python3


def main():

    def is_anagram(s1, s2):
        """
        Docstring for is_anagram

        :param s1: Description
        :param s2: Description
        """
        def normalize(s):
            s = s.lower()
            return ''.join(ch for ch in s if ch.isalnum())

        a = normalize(s1)
        b = normalize(s2)
        return sorted(a) == sorted(b)


if __name__ == "__main__":
    main()
