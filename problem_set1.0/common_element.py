#!/usr/bin/env python3
"""common_element.py

Check if two sets have any elements in common.

"""


def have_common_elements(set1, set2):
    """
    Check if two sets have any elements in common.
    
    Args:
        set1: First collection of elements (can be list, tuple, set, etc.)
        set2: Second collection of elements (can be list, tuple, set, etc.)
        
    Returns:
        bool: True if there are common elements, False otherwise
        
    Examples:
        >>> have_common_elements({1, 2, 3}, {3, 4, 5})
        True
        >>> have_common_elements([1, 2, 3], [4, 5, 6])
        False
        >>> have_common_elements("hello", "world")
        True
    """
    # Convert to sets if not already sets
    if not isinstance(set1, set):
        set1 = set(set1)
    if not isinstance(set2, set):
        set2 = set(set2)
    
    # Check for intersection
    return bool(set1 & set2)


def find_common_elements(collection1, collection2):
    """
    Find and return all common elements between two collections.
    
    Args:
        collection1: First collection of elements
        collection2: Second collection of elements
        
    Returns:
        set: Set of common elements
        
    Examples:
        >>> find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        {3, 4}
        >>> find_common_elements("hello", "world")
        {'l', 'o'}
    """
    return set(collection1) & set(collection2)


def count_common_elements(collection1, collection2):
    """
    Count the number of common elements between two collections.
    
    Args:
        collection1: First collection of elements
        collection2: Second collection of elements
        
    Returns:
        int: Number of common elements
        
    Examples:
        >>> count_common_elements([1, 2, 3], [2, 3, 4])
        2
        >>> count_common_elements("abc", "def")
        0
    """
    return len(set(collection1) & set(collection2))


def have_common_elements_loop(collection1, collection2):
    """
    Check for common elements using a loop approach (educational).
    
    This method demonstrates the algorithmic approach without set operations.
    
    Args:
        collection1: First collection of elements
        collection2: Second collection of elements
        
    Returns:
        bool: True if there are common elements, False otherwise
    """
    # Convert second collection to set for O(1) lookup
    set2 = set(collection2)
    
    # Check each element in first collection
    for element in collection1:
        if element in set2:
            return True
    
    return False


def analyze_common_elements(collection1, collection2):
    """
    Provide detailed analysis of common elements between two collections.
    
    Args:
        collection1: First collection of elements
        collection2: Second collection of elements
        
    Returns:
        dict: Dictionary with analysis results
    """
    set1 = set(collection1)
    set2 = set(collection2)
    common = set1 & set2
    
    return {
        'has_common': bool(common),
        'common_elements': common,
        'count': len(common),
        'unique_to_first': set1 - set2,
        'unique_to_second': set2 - set1,
        'all_elements': set1 | set2,
        'symmetric_difference': set1 ^ set2,
        'jaccard_similarity': len(common) / len(set1 | set2) if set1 | set2 else 0
    }


def display_analysis(analysis, name1="Set 1", name2="Set 2"):
    """
    Display the analysis results in a formatted way.
    
    Args:
        analysis: Dictionary from analyze_common_elements
        name1: Name for first set
        name2: Name for second set
    """
    print("\n" + "="*50)
    print("COMMON ELEMENTS ANALYSIS")
    print("="*50)
    
    if analysis['has_common']:
        print(f"✅ Common elements found: {analysis['common_elements']}")
        print(f"   Count: {analysis['count']}")
    else:
        print("❌ No common elements found")
    
    print(f"\n📊 Detailed Analysis:")
    print(f"   Unique to {name1}: {analysis['unique_to_first']}")
    print(f"   Unique to {name2}: {analysis['unique_to_second']}")
    print(f"   All unique elements: {analysis['all_elements']}")
    print(f"   Symmetric difference: {analysis['symmetric_difference']}")
    print(f"   Jaccard similarity: {analysis['jaccard_similarity']:.2%}")
    print("="*50)


def get_user_input():
    """
    Get two collections from user input with automatic type detection.
    
    Returns:
        tuple: (collection1, collection2, input_type)
    """
    print("\n" + "="*50)
    print("COMMON ELEMENTS CHECKER")
    print("="*50)
    print("\nEnter two collections to check for common elements.")
    print("Examples: '1 2 3 4' or 'apple,banana,orange' or 'hello'")
    
    # Get first input
    input1 = input("\nEnter first collection: ").strip()
    
    # Get second input
    input2 = input("Enter second collection: ").strip()
    
    # Detect input type and parse accordingly
    def parse_input(text):
        """Parse input based on detected format."""
        # Check if it's comma-separated
        if ',' in text:
            return [item.strip() for item in text.split(',')], "comma-separated items"
        # Check if it's space-separated numbers
        elif ' ' in text:
            try:
                return [int(item) for item in text.split()], "numbers"
            except ValueError:
                # Not numbers, treat as space-separated strings
                return text.split(), "words"
        # Check if it's a single number
        else:
            try:
                return [int(text)], "single number"
            except ValueError:
                # Treat as a string (character collection)
                return text, "string/characters"
    
    collection1, type1 = parse_input(input1)
    collection2, type2 = parse_input(input2)
    
    # Determine overall input type
    if type1 == "string/characters" or type2 == "string/characters":
        input_type = "characters"
    elif type1 == "numbers" and type2 == "numbers":
        input_type = "numbers"
    else:
        input_type = "mixed"
    
    return collection1, collection2, input_type


def run_user_check():
    """
    Run a single check with user input and display results.
    """
    collection1, collection2, input_type = get_user_input()
    
    # Perform analysis
    analysis = analyze_common_elements(collection1, collection2)
    
    # Display inputs
    print("\n" + "-"*50)
    print("📥 Your Input:")
    print(f"   Collection 1: {collection1}")
    print(f"   Collection 2: {collection2}")
    print(f"   Type: {input_type}")
    
    # Display results
    print("\n" + "-"*50)
    print("📊 Results:")
    
    if analysis['has_common']:
        print(f"\n✅ YES - Common elements found!")
        print(f"   Common elements: {analysis['common_elements']}")
        print(f"   Number of common elements: {analysis['count']}")
    else:
        print(f"\n❌ NO - No common elements found")
    
    # Additional details
    if analysis['unique_to_first']:
        print(f"\n📌 Only in first: {analysis['unique_to_first']}")
    if analysis['unique_to_second']:
        print(f"📌 Only in second: {analysis['unique_to_second']}")
    
    if analysis['has_common']:
        print(f"\n📈 Similarity: {analysis['jaccard_similarity']:.1%}")
    
    print("="*50)


def main():
    """
    Main function - runs user input mode by default.
    """
    while True:
        run_user_check()
        
        # Ask if user wants to check another pair
        print("\nWould you like to check another pair?")
        again = input("Enter 'y' for yes, any other key to exit: ").strip().lower()
        
        if again != 'y':
            print("\nThank you for using Common Elements Checker!")
            print("Goodbye! 👋")
            break
        
        print()  # Add blank line before next iteration


if __name__ == "__main__":
    main()

