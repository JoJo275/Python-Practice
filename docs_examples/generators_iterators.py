"""
Generators and Iterators Guide
==============================

Understanding lazy evaluation and memory-efficient iteration in Python.
"""

# 1. Iterator Basics
print("=== Iterator Basics ===")

# Any iterable can be converted to an iterator
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator) would raise StopIteration


# 2. Generator Functions (yield)
print("\n=== Generator Functions ===")

def count_up_to(n):
    """Generate numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i  # Pause here and return value
        i += 1

# Generators are lazy - values computed on demand
counter = count_up_to(5)
print(f"Type: {type(counter)}")  # <class 'generator'>

for num in counter:
    print(num, end=" ")  # 1 2 3 4 5
print()


# 3. Generator Expressions
print("\n=== Generator Expressions ===")

# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression - computes values on demand
squares_gen = (x**2 for x in range(1000000))

print(f"List size: {squares_list.__sizeof__()} bytes")
print(f"Generator size: {squares_gen.__sizeof__()} bytes")

# Use generators for large data
first_ten = [next(squares_gen) for _ in range(10)]
print(f"First 10 squares: {first_ten}")


# 4. Practical Example: Reading Large Files
print("\n=== Large File Processing ===")

def read_large_file(filename):
    """Memory-efficient file reader."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# Demo with a small example
def demo_lines():
    yield "Line 1: Hello"
    yield "Line 2: World"
    yield "Line 3: Python"

for line in demo_lines():
    print(line)


# 5. Generator Pipeline
print("\n=== Generator Pipeline ===")

def numbers():
    for i in range(1, 11):
        yield i

def double(nums):
    for n in nums:
        yield n * 2

def filter_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

# Chain generators together - memory efficient!
pipeline = filter_even(double(numbers()))
print(f"Pipeline result: {list(pipeline)}")  # [4, 8, 12, 16, 20]


# 6. yield from (Delegating to Sub-generators)
print("\n=== yield from ===")

def flatten(nested):
    """Flatten a nested list using yield from."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate to recursive call
        else:
            yield item

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
print(f"Flattened: {list(flatten(nested_list))}")


# 7. Two-Way Communication with send()
print("\n=== Generator send() ===")

def accumulator():
    """Generator that accumulates values sent to it."""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
print(next(acc))      # 0 - Initialize generator
print(acc.send(10))   # 10
print(acc.send(20))   # 30
print(acc.send(5))    # 35


# 8. Infinite Generators
print("\n=== Infinite Generators ===")

def fibonacci():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take only what you need
from itertools import islice

fib_gen = fibonacci()
first_10_fib = list(islice(fib_gen, 10))
print(f"First 10 Fibonacci: {first_10_fib}")


# 9. itertools - Generator Utilities
print("\n=== itertools Highlights ===")

from itertools import count, cycle, repeat, chain, combinations

# count - infinite counter
counter = count(start=1, step=2)
odds = [next(counter) for _ in range(5)]
print(f"Odd numbers: {odds}")  # [1, 3, 5, 7, 9]

# cycle - repeat indefinitely
colors = cycle(['red', 'green', 'blue'])
cycled = [next(colors) for _ in range(6)]
print(f"Cycled colors: {cycled}")

# chain - combine iterables
combined = list(chain([1, 2], [3, 4], [5]))
print(f"Chained: {combined}")  # [1, 2, 3, 4, 5]

# combinations
combos = list(combinations('ABC', 2))
print(f"Combinations: {combos}")  # [('A', 'B'), ('A', 'C'), ('B', 'C')]


# 10. Custom Iterator Class
print("\n=== Custom Iterator Class ===")

class Countdown:
    """Iterator that counts down from n to 0."""
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(f"Countdown: {list(Countdown(5))}")  # [5, 4, 3, 2, 1, 0]


# Summary
print("\n=== When to Use Generators ===")
summary = """
Use generators when:
  - Processing large datasets that don't fit in memory
  - Reading large files line by line
  - Creating data pipelines
  - Implementing infinite sequences
  - Lazy evaluation is beneficial

Use lists when:
  - You need random access (indexing)
  - You need to iterate multiple times
  - The data is small enough to fit in memory
  - You need list-specific methods (sort, reverse, etc.)
"""
print(summary)
