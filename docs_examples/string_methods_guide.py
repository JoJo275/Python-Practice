"""
String Methods Quick Reference Guide
====================================

A collection of commonly used Python string methods with examples.
"""

# 1. Case Conversion Methods
text = "Hello World"

print("=== Case Conversion ===")
print(f"upper(): {text.upper()}")        # HELLO WORLD
print(f"lower(): {text.lower()}")        # hello world
print(f"title(): {text.title()}")        # Hello World
print(f"capitalize(): {text.capitalize()}")  # Hello world
print(f"swapcase(): {text.swapcase()}")  # hELLO wORLD

# 2. Search and Find Methods
print("\n=== Search Methods ===")
sentence = "The quick brown fox jumps over the lazy dog"

print(f"find('fox'): {sentence.find('fox')}")        # 16
print(f"index('fox'): {sentence.index('fox')}")      # 16
print(f"count('the'): {sentence.lower().count('the')}")  # 2
print(f"startswith('The'): {sentence.startswith('The')}")  # True
print(f"endswith('dog'): {sentence.endswith('dog')}")      # True

# 3. Strip and Clean Methods
print("\n=== Strip Methods ===")
messy = "   spacious text   "

print(f"strip(): '{messy.strip()}'")      # 'spacious text'
print(f"lstrip(): '{messy.lstrip()}'")    # 'spacious text   '
print(f"rstrip(): '{messy.rstrip()}'")    # '   spacious text'

# 4. Split and Join Methods
print("\n=== Split and Join ===")
csv_data = "apple,banana,cherry"
words = csv_data.split(",")
print(f"split(','): {words}")             # ['apple', 'banana', 'cherry']
print(f"join: {' | '.join(words)}")       # apple | banana | cherry

# 5. Replace Method
print("\n=== Replace ===")
original = "I like cats. Cats are great."
print(f"replace(): {original.replace('cats', 'dogs', 1)}")

# 6. Validation Methods
print("\n=== Validation Methods ===")
test_strings = ["Hello123", "12345", "Hello", "   ", "hello_world"]

for s in test_strings:
    print(f"'{s}': isalnum={s.isalnum()}, isalpha={s.isalpha()}, "
          f"isdigit={s.isdigit()}, isspace={s.isspace()}")

# 7. Formatting Methods
print("\n=== Formatting ===")
name = "python"
print(f"center(20, '-'): {name.center(20, '-')}")
print(f"ljust(20, '.'): {name.ljust(20, '.')}")
print(f"rjust(20, '.'): {name.rjust(20, '.')}")
print(f"zfill(10): {'42'.zfill(10)}")


if __name__ == "__main__":
    print("\n✅ String methods guide executed successfully!")
