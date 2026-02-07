"""
Dictionary Methods Guide
========================

Master Python dictionaries - the most versatile data structure.
"""

# 1. Creating Dictionaries
print("=== Creating Dictionaries ===")

# Literal syntax
person = {"name": "Alice", "age": 30, "city": "NYC"}

# dict() constructor
scores = dict(math=95, science=87, english=92)

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_tuples = dict(pairs)

# Dict comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 2. Accessing Values
print("\n=== Accessing Values ===")

data = {"name": "Bob", "age": 25}

# Direct access (raises KeyError if missing)
print(f"Name: {data['name']}")

# get() - returns None or default if missing
print(f"City: {data.get('city')}")           # None
print(f"City: {data.get('city', 'Unknown')}") # Unknown

# setdefault() - get value or set default if missing
data.setdefault("country", "USA")
print(f"Country: {data['country']}")  # USA


# 3. Adding and Updating
print("\n=== Adding and Updating ===")

inventory = {"apples": 10, "bananas": 5}

# Single item
inventory["oranges"] = 8

# update() - merge dictionaries
inventory.update({"apples": 15, "grapes": 12})
print(f"Inventory: {inventory}")

# Python 3.9+ merge operators
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2        # New dict, dict2 wins conflicts
print(f"Merged: {merged}")    # {'a': 1, 'b': 3, 'c': 4}

dict1 |= dict2                # In-place update
print(f"Updated: {dict1}")


# 4. Removing Items
print("\n=== Removing Items ===")

data = {"a": 1, "b": 2, "c": 3, "d": 4}

# pop() - remove and return value
value = data.pop("a")
print(f"Popped 'a': {value}")

# pop() with default (no KeyError)
value = data.pop("z", "not found")
print(f"Popped 'z': {value}")

# popitem() - remove last inserted item (Python 3.7+)
last = data.popitem()
print(f"Last item: {last}")

# del - remove by key
del data["b"]
print(f"After deletions: {data}")

# clear() - remove all items
data.clear()
print(f"After clear: {data}")


# 5. Iteration Methods
print("\n=== Iteration Methods ===")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Keys (default iteration)
print("Keys:", list(scores.keys()))

# Values
print("Values:", list(scores.values()))

# Items (key-value pairs)
print("Items:", list(scores.items()))

# Unpacking in loops
for name, score in scores.items():
    print(f"  {name}: {score}")


# 6. Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")

# Transform values
doubled = {k: v * 2 for k, v in scores.items()}
print(f"Doubled: {doubled}")

# Filter items
high_scores = {k: v for k, v in scores.items() if v >= 90}
print(f"High scores: {high_scores}")

# Swap keys and values
inverted = {v: k for k, v in scores.items()}
print(f"Inverted: {inverted}")

# From two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "NYC"]
combined = dict(zip(keys, values))
print(f"Zipped: {combined}")


# 7. Membership and Comparison
print("\n=== Membership and Comparison ===")

data = {"a": 1, "b": 2}

# Check key existence
print(f"'a' in data: {'a' in data}")      # True
print(f"'z' in data: {'z' in data}")      # False

# Check value existence
print(f"1 in values: {1 in data.values()}")  # True

# Equality (order doesn't matter)
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(f"d1 == d2: {d1 == d2}")  # True


# 8. Nested Dictionaries
print("\n=== Nested Dictionaries ===")

users = {
    "user1": {"name": "Alice", "email": "alice@example.com"},
    "user2": {"name": "Bob", "email": "bob@example.com"}
}

# Access nested values
print(f"User1 email: {users['user1']['email']}")

# Safe nested access
def get_nested(d, *keys, default=None):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d

print(f"Safe access: {get_nested(users, 'user1', 'phone', default='N/A')}")


# 9. defaultdict - Auto-initialize Missing Keys
print("\n=== defaultdict ===")

from collections import defaultdict

# List as default
groups = defaultdict(list)
for item in [("a", 1), ("b", 2), ("a", 3), ("b", 4)]:
    groups[item[0]].append(item[1])
print(f"Grouped: {dict(groups)}")  # {'a': [1, 3], 'b': [2, 4]}

# Int as default (counting)
counts = defaultdict(int)
for char in "mississippi":
    counts[char] += 1
print(f"Counts: {dict(counts)}")


# 10. Counter - Specialized Counting Dict
print("\n=== Counter ===")

from collections import Counter

# Count elements
word_counts = Counter("abracadabra")
print(f"Letter counts: {word_counts}")

# Most common
print(f"Most common: {word_counts.most_common(2)}")  # [('a', 5), ('b', 2)]

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"c1 + c2: {c1 + c2}")  # Counter({'a': 4, 'b': 3})
print(f"c1 - c2: {c1 - c2}")  # Counter({'a': 2})


# 11. Sorting Dictionaries
print("\n=== Sorting ===")

scores = {"Charlie": 92, "Alice": 95, "Bob": 87}

# Sort by key
by_key = dict(sorted(scores.items()))
print(f"By key: {by_key}")

# Sort by value
by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(f"By value (asc): {by_value}")

# Sort by value descending
by_value_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"By value (desc): {by_value_desc}")


# Summary
print("\n=== Quick Reference ===")
reference = """
d.get(k, default)     - Safe access with default
d.setdefault(k, v)    - Get or set if missing
d.update(other)       - Merge dictionaries
d.pop(k, default)     - Remove and return
d.keys/values/items() - Iteration views
dict1 | dict2         - Merge (Python 3.9+)
defaultdict(factory)  - Auto-initialize missing keys
Counter(iterable)     - Count occurrences
"""
print(reference)
