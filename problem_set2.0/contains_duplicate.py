#!/usr/bin/env python3
"""contains_duplicate.py

Contains Duplicate - A beginner-friendly implementation.

What does "Contains Duplicate" mean?
------------------------------------
This program checks if a list has any repeated (duplicate) values.

Examples:
- [1, 2, 3, 1] contains a duplicate (1 appears twice)
- [1, 2, 3, 4] does NOT contain duplicates (all unique)
- ['a', 'b', 'a'] contains a duplicate ('a' appears twice)

This is a common coding interview question!
"""


def contains_duplicate_simple(numbers):
    """
    Check if a list contains any duplicate values using a set.
    
    How this works:
    ---------------
    A "set" in Python is a collection that cannot have duplicates.
    If we convert a list to a set, duplicates are automatically removed.
    
    So if the set is smaller than the original list, there were duplicates!
    
    Args:
        numbers (list): A list of values to check
    
    Returns:
        bool: True if there are duplicates, False if all values are unique
    
    Example:
        >>> contains_duplicate_simple([1, 2, 3, 1])
        True
        >>> contains_duplicate_simple([1, 2, 3, 4])
        False
    """
    # Convert the list to a set
    # Sets automatically remove duplicates
    # Example: [1, 2, 1] becomes {1, 2}
    unique_values = set(numbers)
    
    # Compare lengths:
    # - If set is smaller, some duplicates were removed
    # - If lengths are equal, all values were unique
    original_length = len(numbers)
    unique_length = len(unique_values)
    
    # Return True if there are duplicates (lengths are different)
    return original_length != unique_length


def contains_duplicate_loop(numbers):
    """
    Check if a list contains duplicates using a loop.
    
    How this works:
    ---------------
    We go through each item and keep track of what we've seen.
    If we see something we've already seen, it's a duplicate!
    
    This method is easier to understand step-by-step.
    
    Args:
        numbers (list): A list of values to check
    
    Returns:
        bool: True if there are duplicates, False if all values are unique
    
    Example:
        >>> contains_duplicate_loop([1, 2, 3, 1])
        True
    """
    # Create an empty set to store values we've seen
    # We use a set because checking "if x in set" is very fast
    seen = set()
    
    # Look at each number in the list
    for number in numbers:
        # Check if we've seen this number before
        if number in seen:
            # Yes! It's a duplicate!
            return True
        else:
            # No, this is new. Remember it for later.
            seen.add(number)
    
    # We checked everything and found no duplicates
    return False


def find_duplicates(numbers):
    """
    Find and return all duplicate values in a list.
    
    This is a bonus function that tells you WHICH values are duplicated.
    
    Args:
        numbers (list): A list of values to check
    
    Returns:
        list: A list of values that appear more than once
    
    Example:
        >>> find_duplicates([1, 2, 2, 3, 3, 3])
        [2, 3]
    """
    # Keep track of what we've seen and what's duplicated
    seen = set()
    duplicates = set()
    
    # Go through each number
    for number in numbers:
        if number in seen:
            # We've seen it before, so it's a duplicate
            duplicates.add(number)
        else:
            # First time seeing it
            seen.add(number)
    
    # Convert set to list and return
    return list(duplicates)


def count_duplicates(numbers):
    """
    Count how many times each value appears in the list.
    
    Args:
        numbers (list): A list of values to check
    
    Returns:
        dict: A dictionary showing each value and its count
    
    Example:
        >>> count_duplicates([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
    """
    # Create an empty dictionary to store counts
    counts = {}
    
    # Count each number
    for number in numbers:
        if number in counts:
            # We've seen this before, add 1 to its count
            counts[number] = counts[number] + 1
        else:
            # First time seeing it, count is 1
            counts[number] = 1
    
    return counts


def main():
    """
    Main function to run the duplicate checker program.
    
    This function:
    1. Welcomes the user
    2. Gets a list of numbers from the user
    3. Checks for duplicates
    4. Displays the results
    """
    # Print welcome message
    print("=" * 50)
    print("DUPLICATE CHECKER")
    print("=" * 50)
    print("\nThis program checks if a list contains duplicates.")
    print("A duplicate is any value that appears more than once.\n")
    
    # Keep running until user wants to quit
    while True:
        print("-" * 50)
        print("\nEnter numbers separated by spaces.")
        print("Example: 1 2 3 4 5")
        print("Or type 'quit' to exit.\n")
        
        # Get input from user
        user_input = input("Your numbers: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("\nThank you for using Duplicate Checker!")
            print("Goodbye! 👋")
            break
        
        # Try to convert input to a list of numbers
        try:
            # Split the input by spaces and convert each to integer
            numbers = [int(x) for x in user_input.split()]
            
            # Check if user entered any numbers
            if len(numbers) == 0:
                print("\n⚠️ Please enter at least one number.")
                continue
            
        except ValueError:
            # User entered something that isn't a number
            print("\n⚠️ Invalid input. Please enter numbers only.")
            print("   Example: 1 2 3 4 5")
            continue
        
        # Display the list they entered
        print(f"\nYour list: {numbers}")
        print(f"Length: {len(numbers)} items")
        
        # Check for duplicates
        has_duplicates = contains_duplicate_simple(numbers)
        
        # Display results
        print("\n" + "-" * 30)
        print("RESULT:")
        print("-" * 30)
        
        if has_duplicates:
            print("✓ YES - This list contains duplicates!")
            
            # Show which values are duplicated
            duplicates = find_duplicates(numbers)
            print(f"\n  Duplicate values: {duplicates}")
            
            # Show counts for each value
            counts = count_duplicates(numbers)
            print("\n  Count of each value:")
            for value, count in sorted(counts.items()):
                if count > 1:
                    print(f"    {value} appears {count} times ← duplicate")
                else:
                    print(f"    {value} appears {count} time")
        else:
            print("✗ NO - All values are unique. No duplicates found.")
            
            # Show unique values
            print(f"\n  Unique values: {sorted(set(numbers))}")
        
        print("-" * 30)


def demonstrate_examples():
    """
    Show examples to help users understand how duplicates work.
    """
    print("\n" + "=" * 50)
    print("EXAMPLES")
    print("=" * 50)
    
    # Example lists to demonstrate
    examples = [
        [1, 2, 3, 1],           # Has duplicate
        [1, 2, 3, 4],           # No duplicates
        [1, 1, 1, 1],           # All same
        [5],                     # Single element
        [],                      # Empty list
        [1, 2, 3, 4, 5, 1, 2],  # Multiple duplicates
    ]
    
    for example in examples:
        has_dup = contains_duplicate_simple(example)
        symbol = "✓ YES" if has_dup else "✗ NO"
        print(f"\n{example}")
        print(f"  Contains duplicates? {symbol}")
        
        if has_dup:
            dups = find_duplicates(example)
            print(f"  Duplicated values: {dups}")
    
    print("\n" + "=" * 50)


# This runs when the file is executed directly
if __name__ == "__main__":
    # Uncomment below to see examples first
    # demonstrate_examples()
    
    # Run the main program
    main()

