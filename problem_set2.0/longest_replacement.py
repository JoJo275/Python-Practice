#!/usr/bin/env python3
"""longest_replacement.py

Longest Repeating Character Replacement - A beginner-friendly implementation.

What is this problem?
---------------------
Given a string and a number k, find the longest substring where you can
replace at most k characters to make all characters the same.

Example:
- String: "AABABBA", k = 1
- Answer: 4 (the substring "AABA" - replace one B with A to get "AAAA")

Why is this useful?
-------------------
This is a classic "sliding window" problem that teaches you:
- How to efficiently scan through a string
- How to track character counts
- How to expand and shrink a "window" of characters

This is a common coding interview question!
"""


def longest_repeating_character_replacement(s, k):
    """
    Find the longest substring with at most k replacements.
    
    How this works (Sliding Window technique):
    ------------------------------------------
    Imagine a "window" that slides across the string:
    
    String: A A B A B B A
            [     ]         <- window
    
    1. Start with an empty window
    2. Expand the window by adding characters from the right
    3. If we need more than k replacements, shrink from the left
    4. Track the maximum window size we achieve
    
    The key insight:
    - Window size - count of most frequent character = replacements needed
    - If replacements needed > k, shrink the window
    
    Args:
        s (str): The input string (usually uppercase letters)
        k (int): Maximum number of characters we can replace
    
    Returns:
        int: Length of the longest valid substring
    
    Example:
        >>> longest_repeating_character_replacement("AABABBA", 1)
        4
        >>> longest_repeating_character_replacement("ABAB", 2)
        4
    """
    # Handle edge case: empty string
    if len(s) == 0:
        return 0
    
    # Keep track of the count of each character in our window
    # Example: {'A': 2, 'B': 1} means 2 A's and 1 B in current window
    char_count = {}
    
    # Left edge of our sliding window
    left = 0
    
    # Track the count of the most frequent character in window
    max_freq = 0
    
    # Track the longest valid window we've found
    result = 0
    
    # Move the right edge across the string
    # 'right' is the index of the character we're adding to window
    for right in range(len(s)):
        # Get the character at the right edge
        char = s[right]
        
        # Add this character to our count
        # If it's new, start at 0, then add 1
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
        
        # Update max frequency if this character is now most common
        if char_count[char] > max_freq:
            max_freq = char_count[char]
        
        # Calculate current window size
        window_size = right - left + 1
        
        # Calculate how many replacements we need
        # Window size - most frequent = characters that need replacing
        replacements_needed = window_size - max_freq
        
        # If we need too many replacements, shrink window from left
        if replacements_needed > k:
            # Remove the leftmost character from our count
            left_char = s[left]
            char_count[left_char] = char_count[left_char] - 1
            
            # Move left edge to the right (shrink window)
            left = left + 1
        
        # Update result with current window size
        # (window might have shrunk, so recalculate)
        current_window_size = right - left + 1
        if current_window_size > result:
            result = current_window_size
    
    return result


def longest_repeating_simple(s, k):
    """
    A simpler (but slower) approach for understanding.
    
    This method checks every possible substring - it's easier to
    understand but less efficient. Use this to learn the concept!
    
    Args:
        s (str): The input string
        k (int): Maximum replacements allowed
    
    Returns:
        int: Length of the longest valid substring
    """
    # Track the best result
    max_length = 0
    
    # Try every possible starting position
    for start in range(len(s)):
        # Try every possible ending position
        for end in range(start, len(s)):
            # Get the substring from start to end
            substring = s[start:end + 1]
            
            # Count each character in this substring
            char_count = {}
            for char in substring:
                if char in char_count:
                    char_count[char] = char_count[char] + 1
                else:
                    char_count[char] = 1
            
            # Find the most common character
            most_common_count = 0
            for count in char_count.values():
                if count > most_common_count:
                    most_common_count = count
            
            # Calculate replacements needed
            replacements_needed = len(substring) - most_common_count
            
            # Check if this substring is valid (needs <= k replacements)
            if replacements_needed <= k:
                # Update max length if this is longer
                if len(substring) > max_length:
                    max_length = len(substring)
    
    return max_length


def visualize_sliding_window(s, k):
    """
    Visualize how the sliding window moves through the string.
    
    This helps you SEE what the algorithm is doing!
    
    Args:
        s (str): The input string
        k (int): Maximum replacements allowed
    """
    print("\n" + "=" * 60)
    print("SLIDING WINDOW VISUALIZATION")
    print("=" * 60)
    print(f"\nString: {s}")
    print(f"Max replacements (k): {k}")
    print("\n" + "-" * 60)
    
    char_count = {}
    left = 0
    max_freq = 0
    result = 0
    
    for right in range(len(s)):
        char = s[right]
        
        # Update count
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1
        
        if char_count[char] > max_freq:
            max_freq = char_count[char]
        
        window_size = right - left + 1
        replacements_needed = window_size - max_freq
        
        # Visualize current state
        window_str = ""
        for i, c in enumerate(s):
            if i == left:
                window_str += "["
            window_str += c
            if i == right:
                window_str += "]"
            elif i >= left and i < right:
                pass  # Inside window
            elif i < left or i > right:
                pass  # Outside window
        
        # Build window display
        display = list(s)
        window_display = " " * left + "[" + s[left:right+1] + "]"
        
        print(f"\nStep {right + 1}:")
        print(f"  String:  {s}")
        print(f"  Window:  {' ' * left}{'[' + s[left:right+1] + ']'}")
        print(f"  Size: {window_size}, Most freq: {max_freq}, Replacements: {replacements_needed}")
        
        if replacements_needed > k:
            # Remove left character
            left_char = s[left]
            char_count[left_char] = char_count[left_char] - 1
            left = left + 1
            print(f"  → Too many replacements! Shrinking window from left.")
        
        current_size = right - left + 1
        if current_size > result:
            result = current_size
            print(f"  → New best! Length = {result}")
    
    print("\n" + "-" * 60)
    print(f"FINAL ANSWER: {result}")
    print("=" * 60)


def main():
    """
    Main function to run the longest replacement program.
    """
    print("=" * 60)
    print("LONGEST REPEATING CHARACTER REPLACEMENT")
    print("=" * 60)
    print("\nThis program finds the longest substring where you can")
    print("replace at most k characters to make all chars the same.\n")
    
    while True:
        print("-" * 60)
        print("\n1. Check a string")
        print("2. See visualization")
        print("3. Run examples")
        print("4. Quit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            # Get string from user
            s = input("\nEnter a string (e.g., AABABBA): ").upper()
            
            # Get k value
            try:
                k = int(input("Enter k (max replacements): "))
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue
            
            # Calculate result
            result = longest_repeating_character_replacement(s, k)
            
            # Display result
            print(f"\n✓ Result: {result}")
            print(f"  You can make a substring of length {result}")
            print(f"  with at most {k} replacements.")
            
        elif choice == '2':
            # Visualization mode
            s = input("\nEnter a string (e.g., AABABBA): ").upper()
            
            try:
                k = int(input("Enter k (max replacements): "))
            except ValueError:
                print("⚠️ Please enter a valid number.")
                continue
            
            visualize_sliding_window(s, k)
            
        elif choice == '3':
            # Run examples
            print("\n" + "=" * 60)
            print("EXAMPLES")
            print("=" * 60)
            
            examples = [
                ("ABAB", 2, 4),
                ("AABABBA", 1, 4),
                ("AAAA", 2, 4),
                ("ABCD", 1, 2),
                ("AAAB", 0, 3),
            ]
            
            for s, k, expected in examples:
                result = longest_repeating_character_replacement(s, k)
                status = "✓" if result == expected else "✗"
                print(f"\n{status} String: '{s}', k={k}")
                print(f"   Answer: {result}")
            
        elif choice == '4':
            print("\nGoodbye! 👋")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")


# Run the program when this file is executed
if __name__ == "__main__":
    main()
