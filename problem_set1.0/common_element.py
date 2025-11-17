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


def interactive_mode():
    """
    Run interactive mode for testing common elements.
    """
    print("\n" + "="*50)
    print("COMMON ELEMENTS CHECKER")
    print("="*50)
    
    while True:
        print("\n1. Check two lists of numbers")
        print("2. Check two strings")
        print("3. Check custom collections")
        print("4. Run examples")
        print("5. Quit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            # Input lists of numbers
            try:
                list1 = input("\nEnter first list (space-separated numbers): ").split()
                list1 = [int(x) for x in list1]
                
                list2 = input("Enter second list (space-separated numbers): ").split()
                list2 = [int(x) for x in list2]
                
                analysis = analyze_common_elements(list1, list2)
                display_analysis(analysis, "List 1", "List 2")
                
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
        
        elif choice == '2':
            # Input strings
            str1 = input("\nEnter first string: ")
            str2 = input("Enter second string: ")
            
            analysis = analyze_common_elements(str1, str2)
            display_analysis(analysis, "String 1", "String 2")
        
        elif choice == '3':
            # Custom input
            try:
                input1 = input("\nEnter first collection (comma-separated): ")
                collection1 = [x.strip() for x in input1.split(',')]
                
                input2 = input("Enter second collection (comma-separated): ")
                collection2 = [x.strip() for x in input2.split(',')]
                
                analysis = analyze_common_elements(collection1, collection2)
                display_analysis(analysis, "Collection 1", "Collection 2")
                
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '4':
            # Run examples
            examples = [
                ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]),
                ("hello", "world"),
                ([1, 2, 3], [4, 5, 6]),
                ("python", "programming"),
                (['a', 'b', 'c'], ['b', 'c', 'd'])
            ]
            
            print("\n" + "="*50)
            print("EXAMPLES")
            print("="*50)
            
            for i, (col1, col2) in enumerate(examples, 1):
                print(f"\nExample {i}:")
                print(f"  Collection 1: {col1}")
                print(f"  Collection 2: {col2}")
                
                common = find_common_elements(col1, col2)
                has_common = have_common_elements(col1, col2)
                
                if has_common:
                    print(f"  ✅ Has common elements: {common}")
                else:
                    print(f"  ❌ No common elements")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-5.")


def main():
    """
    Main function to demonstrate common element checking.
    """
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], [3, 4, 5, 6], "Number Lists"),
        ("hello", "world", "Strings"),
        ({1, 2, 3}, {4, 5, 6}, "Disjoint Sets"),
        ([1, 1, 2, 2], [2, 2, 3, 3], "Lists with Duplicates"),
        ([], [1, 2, 3], "Empty vs Non-empty"),
        ("", "abc", "Empty String"),
        (range(5), range(3, 8), "Ranges")
    ]
    
    print("="*50)
    print("COMMON ELEMENTS CHECKER - TEST SUITE")
    print("="*50)
    
    for col1, col2, description in test_cases:
        print(f"\nTest: {description}")
        print(f"  Collection 1: {list(col1) if hasattr(col1, '__iter__') and not isinstance(col1, str) else col1}")
        print(f"  Collection 2: {list(col2) if hasattr(col2, '__iter__') and not isinstance(col2, str) else col2}")
        
        has_common = have_common_elements(col1, col2)
        if has_common:
            common = find_common_elements(col1, col2)
            count = count_common_elements(col1, col2)
            print(f"  Result: ✅ Has {count} common element(s): {common}")
        else:
            print(f"  Result: ❌ No common elements")
    
    print("\n" + "-"*50)
    print("Run with 'python common_element.py -i' for interactive mode")


if __name__ == "__main__":
    # Check for command line arguments without importing sys
    try:
        # Try to access command line argument
        import sys
        if len(sys.argv) > 1 and sys.argv[1] in ['-i', '--interactive']:
            interactive_mode()
        else:
            main()
    except:
        # If sys import fails or no arguments, just run main
        main()

