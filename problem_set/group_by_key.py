"""group_by_key.py

5) group_by_key(items, key)
- Description: Given a list of dicts `items` and a `key` string, return a dict
mapping key values to lists of items with that key. If an item doesn't have
the key, group under None.

- Input: list of dicts, string key
- Output: dict

"""

# !/usr/bin/env python3


def main() -> None:
    items = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 30},
    ]
    key = "age"
    grouped = group_by_key(items, key)
    print(grouped)

def group_by_key(items: list[dict], key: str) -> dict:
    """Group a list of dictionaries by a specified key.

    Args:
        items: A list of dictionaries to be grouped.
        key: The key to group the dictionaries by.

    Returns:
        A dictionary mapping key values to lists of dictionaries that share that key value.
        If a dictionary does not contain the specified key, it is grouped under None.

    Examples:
        >>> items = [
        ...     {"name": "Alice", "age": 30},
        ...     {"name": "Bob", "age": 25},
        ...     {"name": "Charlie", "age": 35},
        ...     {"name": "David", "age": 30},
        ... ]
        >>> group_by_key(items, "age")
        {
            25: [{"name": "Bob", "age": 25}],
            30: [{"name": "Alice", "age": 30}, {"name": "David", "age": 30}],
            35: [{"name": "Charlie", "age": 35}]
        }
        >>> group_by_key(items, "name")
        {
            "Alice": [{"name": "Alice", "age": 30}],
            "Bob": [{"name": "Bob", "age": 25}],
            "Charlie": [{"name": "Charlie", "age": 35}],
            "David": [{"name": "David", "age": 30}]
        }
    """
    grouped = {}
    for item in items:
        key_value = item.get(key, None)
        if key_value not in grouped:
            grouped[key_value] = []
        grouped[key_value].append(item)
    return grouped


if __name__ == "__main__":
    main()
