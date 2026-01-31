"""
List Comprehensions Cheat Sheet
===============================

Master Python list comprehensions with these practical examples.
"""

# Basic Syntax: [expression for item in iterable]

# 1. Simple Transformations
print("=== Simple Transformations ===")
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]
print(f"Squares: {squares}")  # [1, 4, 9, 16, 25]

doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")  # [2, 4, 6, 8, 10]


# 2. With Conditionals (Filtering)
print("\n=== Filtering ===")
nums = range(1, 21)

evens = [x for x in nums if x % 2 == 0]
print(f"Even numbers: {evens}")

divisible_by_3 = [x for x in nums if x % 3 == 0]
print(f"Divisible by 3: {divisible_by_3}")


# 3. If-Else in Comprehensions
print("\n=== If-Else (Ternary) ===")
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print(f"Labels: {labels}")  # ['odd', 'even', 'odd', 'even', 'odd']

capped = [x if x < 5 else 5 for x in [1, 3, 5, 7, 9]]
print(f"Capped at 5: {capped}")  # [1, 3, 5, 5, 5]


# 4. Nested Loops
print("\n=== Nested Loops ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(f"Pairs: {pairs}")  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


# 5. String Operations
print("\n=== String Operations ===")
words = ["hello", "world", "python"]

upper_words = [w.upper() for w in words]
print(f"Uppercase: {upper_words}")

lengths = [len(w) for w in words]
print(f"Lengths: {lengths}")

first_chars = [w[0] for w in words]
print(f"First chars: {first_chars}")


# 6. Dictionary Comprehensions
print("\n=== Dict Comprehensions ===")
names = ["alice", "bob", "charlie"]

name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")

squared_dict = {x: x**2 for x in range(1, 6)}
print(f"Squared dict: {squared_dict}")


# 7. Set Comprehensions
print("\n=== Set Comprehensions ===")
text = "hello world"
unique_chars = {char for char in text if char.isalpha()}
print(f"Unique letters: {unique_chars}")


# 8. Practical Examples
print("\n=== Practical Examples ===")

# Extract emails from data
users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]
emails = [user["email"] for user in users]
print(f"Emails: {emails}")

# Filter and transform
scores = [85, 92, 78, 95, 88, 72, 90]
passing_grades = [f"Pass ({s})" for s in scores if s >= 80]
print(f"Passing: {passing_grades}")


if __name__ == "__main__":
    print("\n✅ List comprehensions guide executed successfully!")
