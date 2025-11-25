#!/usr/bin/env python3
"""valid_anagram.py

Valid Anagram - A beginner-friendly implementation.

What is an Anagram?
-------------------
An anagram is a word or phrase formed by rearranging the letters of another
word or phrase, using all the original letters exactly once.

Examples:
- "listen" and "silent" are anagrams
- "rat" and "tar" are anagrams
- "hello" and "world" are NOT anagrams

This program checks if two strings are anagrams of each other.
"""


def is_anagram_simple(word1, word2):
    """
    Check if two words are anagrams using the sorting method.

    This is the simplest approach for beginners:
    1. Convert both words to lowercase (so 'A' and 'a' are treated the same)
    2. Remove any spaces (for phrases)
    3. Sort the letters of both words
    4. Compare if they're equal

    Args:
        word1 (str): The first word or phrase
        word2 (str): The second word or phrase

    Returns:
        bool: True if the words are anagrams, False otherwise

    Example:
        >>> is_anagram_simple("listen", "silent")
        True
        >>> is_anagram_simple("hello", "world")
        False
    """
    # Step 1: Clean the words - remove spaces and convert to lowercase
    # This ensures "Listen" and "silent" are treated the same
    clean_word1 = word1.replace(" ", "").lower()
    clean_word2 = word2.replace(" ", "").lower()

    # Step 2: Quick check - if lengths are different, they can't be anagrams
    # An anagram must use ALL letters exactly once
    if len(clean_word1) != len(clean_word2):
        return False

    # Step 3: Sort the letters of both words
    # sorted() function returns a list of characters in alphabetical order
    # For example: sorted("cat") returns ['a', 'c', 't']
    sorted_word1 = sorted(clean_word1)
    sorted_word2 = sorted(clean_word2)

    # Step 4: Compare the sorted lists
    # If they're the same, the words are anagrams
    return sorted_word1 == sorted_word2


def is_anagram_counting(word1, word2):
    """
    Check if two words are anagrams by counting characters.

    This method counts how many times each letter appears:
    1. Count each letter in word1
    2. Count each letter in word2
    3. Compare if the counts are the same

    Args:
        word1 (str): The first word or phrase
        word2 (str): The second word or phrase

    Returns:
        bool: True if the words are anagrams, False otherwise

    Example:
        >>> is_anagram_counting("rat", "tar")
        True
    """
    # Clean the words
    clean_word1 = word1.replace(" ", "").lower()
    clean_word2 = word2.replace(" ", "").lower()

    # Quick length check
    if len(clean_word1) != len(clean_word2):
        return False

    # Create dictionaries to count characters
    # A dictionary stores key-value pairs, like {'a': 2, 'b': 1}
    char_count1 = {}
    char_count2 = {}

    # Count characters in word1
    for char in clean_word1:
        # If we've seen this character before, add 1 to its count
        # If we haven't seen it, start counting at 1
        if char in char_count1:
            char_count1[char] = char_count1[char] + 1
        else:
            char_count1[char] = 1

    # Count characters in word2
    for char in clean_word2:
        if char in char_count2:
            char_count2[char] = char_count2[char] + 1
        else:
            char_count2[char] = 1

    # Compare the two dictionaries
    return char_count1 == char_count2


def main():
    """
    Main function to run the anagram checker program.

    This function:
    1. Welcomes the user
    2. Gets two words from the user
    3. Checks if they're anagrams
    4. Displays the result
    """
    # Print welcome message
    print("=" * 50)
    print("ANAGRAM CHECKER")
    print("=" * 50)
    print("\nAn anagram is formed by rearranging letters.")
    print("For example: 'listen' and 'silent' are anagrams.\n")

    # Keep running until user wants to quit
    while True:
        # Get input from user
        print("-" * 50)
        word1 = input("Enter the first word or phrase: ")
        word2 = input("Enter the second word or phrase: ")

        # Check if they're anagrams using the simple method
        result = is_anagram_simple(word1, word2)

        # Display the result with clear formatting
        print("\nResult:")
        if result:
            print(f"✓ YES! '{word1}' and '{word2}' ARE anagrams!")

            # Show the sorted letters to help understand why
            sorted1 = ''.join(sorted(word1.replace(" ", "").lower()))
            sorted2 = ''.join(sorted(word2.replace(" ", "").lower()))
            print(f"  Both contain the letters: {sorted1}")
        else:
            print(f"✗ NO! '{word1}' and '{word2}' are NOT anagrams.")

            # Explain why they're not anagrams
            if len(word1.replace(" ", "")) != len(word2.replace(" ", "")):
                print(f"  Reason: Different lengths ({len(word1.replace(' ", ''))} vs {len(word2.replace(' ", ''))} letters)")
            else:
                print("  Reason: Different letters or different counts")

        # Ask if user wants to check another pair
        print("\n" + "-" * 50)
        continue_choice = input("Check another pair? (yes/no): ").lower()

        # Exit if user says no (or anything that starts with 'n')
        if continue_choice.startswith('n'):
            print("\nThank you for using Anagram Checker!")
            print("Goodbye! 👋")
            break

        print()  # Empty line for spacing


def demonstrate_examples():
    """
    Show examples of anagrams to help users understand.

    This function is educational - it shows various examples
    of what are and aren't anagrams.
    """
    print("\n" + "=" * 50)
    print("ANAGRAM EXAMPLES")
    print("=" * 50)

    # List of example pairs: (word1, word2, expected_result)
    examples = [
        ("listen", "silent", True),
        ("rat", "tar", True),
        ("evil", "vile", True),
        ("a gentleman", "elegant man", True),
        ("hello", "world", False),
        ("python", "java", False),
        ("study", "dusty", True),
        ("night", "thing", True),
        ("act", "cat", True),
        ("abc", "xyz", False)
    ]

    print("\nChecking example pairs:\n")

    # Check each example
    for word1, word2, expected in examples:
        result = is_anagram_simple(word1, word2)

        # Use checkmark or X to show result
        symbol = "✓" if result else "✗"
        status = "ARE" if result else "are NOT"

        # Display with nice formatting
        print(f"{symbol} '{word1}' and '{word2}' {status} anagrams")

        # Verify our function works correctly
        if result != expected:
            print(f"   WARNING: Unexpected result!")

    print("\n" + "=" * 50)


# This section only runs if the file is executed directly
# (not if it's imported as a module)
if __name__ == "__main__":
    # Uncomment the line below to see examples first
    # demonstrate_examples()

    # Run the main program
    main()
