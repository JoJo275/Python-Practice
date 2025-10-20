"""flatten.py

4) flatten(lst)
- Description: Given a list which can contain nested lists to arbitrary depth,
return a flattened list with all elements in order.
- Input: list (elements can be lists)
- Output: list

"""

#!/usr/bin/env python3


def main() -> None:
    """Main function to demonstrate flatten usage."""
    example = [1, [2, [3, 4], 5], 6, [[7]], 8]
    print("Original nested list:", example)
    print("Flattened list:", flatten(example))


def flatten(lst: list) -> list:
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
