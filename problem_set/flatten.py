"""flatten.py

4) flatten(lst)
- Description: Given a list which can contain nested lists to arbitrary depth,
return a flattened list with all elements in order.
- Input: list (elements can be lists)
- Output: list

"""

# !/usr/bin/env python3

from typing import Any, List
import ast


def parse_list_input(user_input: str) -> List[Any]:
    """Safely parse user input string into a Python list.

    Args:
        user_input: String representation of a list (e.g., "[1, [2, 3]]").

    Returns:
        Parsed list object.

    Raises:
        ValueError: If input cannot be safely parsed as a list.
        SyntaxError: If input has invalid Python syntax.
    """
    user_input = user_input.strip()

    if not user_input:
        raise ValueError("Input cannot be empty.")

    # Use ast.literal_eval for safe evaluation (no code execution)
    try:
        result = ast.literal_eval(user_input)
    except (ValueError, SyntaxError) as e:
        raise ValueError(
            f"Invalid list format. Please use Python list syntax: {e}"
        )

    # Ensure the result is actually a list
    if not isinstance(result, list):
        raise ValueError(
            f"Input must be a list, got {type(result).__name__} instead."
        )

    return result


def main() -> None:
    """Main function with interactive input and error handling.

    Provides an interactive interface for users to input nested lists
    and see them flattened. Includes comprehensive error handling for
    invalid inputs and edge cases.
    """
    print("=" * 60)
    print("=== Nested List Flattener ===")
    print("=" * 60)
    print("\nThis program flattens nested lists to a single level.")
    print("Example: [1, [2, [3, 4]], 5] becomes [1, 2, 3, 4, 5]")
    print("\nInstructions:")
    print("  - Enter a list using Python syntax: [1, [2, 3], 4]")
    print("  - Lists can be nested to any depth")
    print("  - Type 'q', 'quit', or 'exit' to quit")
    print("  - Press Ctrl+C to exit anytime")
    print("=" * 60)
    print()

    # Pre-defined examples
    examples = [
        [1, [2, [3, 4], 5], 6, [[7]], 8],
        [[1, 2], [3, [4, 5]], 6],
        [1, 2, 3, 4, 5],
        [[[[1]]], 2, [3, [4]]],
    ]

    print("Example demonstrations:")
    for i, example in enumerate(examples, 1):
        result = flatten(example)
        print(f"{i}. {example}")
        print(f"   → {result}")
    print()
    print("=" * 60)
    print()

    while True:
        try:
            # Get user input
            prompt = "Enter a nested list (or 'q' to quit): "
            user_input = input(prompt).strip()

            # Check for quit commands
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("\nThank you for using the List Flattener. Goodbye!")
                break

            # Parse the input
            nested_list = parse_list_input(user_input)

            # Flatten the list
            result = flatten(nested_list)

            # Display results
            print(f"\n✓ Original: {nested_list}")
            print(f"✓ Flattened: {result}")
            print(f"✓ Original depth: {_get_depth(nested_list)} levels")
            print(f"✓ Total elements: {len(result)}")
            print()

        except ValueError as e:
            print(f"\n✗ Error: {e}")
            print("  Hint: Use Python list syntax like [1, [2, 3], 4]\n")

        except SyntaxError as e:
            print("\n✗ Syntax Error: Invalid list format")
            print(f"  Details: {e}")
            print("  Hint: Make sure brackets are balanced\n")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break

        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
            print("  Please try again with a valid list.\n")


def _get_depth(lst: List[Any]) -> int:
    """Calculate the maximum nesting depth of a list.

    Args:
        lst: A list that may contain nested lists.

    Returns:
        The maximum depth of nesting (1 for a flat list).

    Examples:
        >>> _get_depth([1, 2, 3])
        1
        >>> _get_depth([1, [2, 3]])
        2
        >>> _get_depth([1, [2, [3, 4]]])
        3
    """
    if not isinstance(lst, list):
        return 0

    if not lst:
        return 1

    max_depth = 1
    for item in lst:
        if isinstance(item, list):
            depth = 1 + _get_depth(item)
            max_depth = max(max_depth, depth)

    return max_depth


def flatten(lst: List[Any]) -> List[Any]:
    """Flatten a nested list to a single-level list.

    Args:
        lst: A list which may contain nested lists.

    Returns:
        A flattened list containing all elements in order.

    Examples:
        >>> flatten([1, [2, [3, 4], 5], 6])
        [1, 2, 3, 4, 5, 6]
        >>> flatten([[1, 2], [3, [4, 5]], 6])
        [1, 2, 3, 4, 5, 6]
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened


if __name__ == "__main__":
    main()
