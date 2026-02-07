"""
Exception Handling Guide
========================

Master Python's try/except pattern for robust error handling.
"""

# 1. Basic Try/Except
print("=== Basic Try/Except ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 2. Catching Multiple Exceptions
print("\n=== Multiple Exceptions ===")

def safe_convert(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"Conversion failed: {e}")
        return None

print(safe_convert("42"))       # 42
print(safe_convert("hello"))    # None (ValueError)
print(safe_convert(None))       # None (TypeError)


# 3. The else Clause
print("\n=== Try/Except/Else ===")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    else:
        # Runs only if no exception occurred
        print(f"{a} / {b} = {result}")

divide(10, 2)
divide(10, 0)


# 4. The finally Clause
print("\n=== Try/Except/Finally ===")

def read_file_demo():
    file = None
    try:
        file = open("nonexistent.txt", "r")
        content = file.read()
    except FileNotFoundError:
        print("File not found!")
    finally:
        # Always runs, even if exception occurs
        if file:
            file.close()
        print("Cleanup complete.")

read_file_demo()


# 5. Raising Exceptions
print("\n=== Raising Exceptions ===")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")


# 6. Custom Exceptions
print("\n=== Custom Exceptions ===")

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")


# 7. Re-raising Exceptions
print("\n=== Re-raising Exceptions ===")

def process_data(data):
    try:
        result = data["key"]
    except KeyError:
        print("Logging: Missing key in data")
        raise  # Re-raise the same exception

try:
    process_data({})
except KeyError:
    print("Handled at higher level")


# 8. Exception Chaining
print("\n=== Exception Chaining ===")

def load_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError("Configuration failed") from e

try:
    load_config("config.yaml")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")


# 9. Context Managers (with statement)
print("\n=== Context Managers ===")

# Automatically handles cleanup - preferred over try/finally
try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!")
    print("File written successfully")
except IOError as e:
    print(f"IO error: {e}")


# 10. Common Exception Types Reference
print("\n=== Common Exception Types ===")

exceptions_reference = """
ValueError      - Wrong value (e.g., int("abc"))
TypeError       - Wrong type (e.g., "2" + 2)
KeyError        - Missing dictionary key
IndexError      - List index out of range
FileNotFoundError - File doesn't exist
AttributeError  - Object has no such attribute
ImportError     - Module import failed
RuntimeError    - Generic runtime error
StopIteration   - Iterator exhausted
"""
print(exceptions_reference)


# Best Practices Summary
print("=== Best Practices ===")
best_practices = """
1. Catch specific exceptions, not bare 'except:'
2. Use 'else' for code that should run only on success
3. Use 'finally' for cleanup (or context managers)
4. Create custom exceptions for domain-specific errors
5. Include meaningful error messages
6. Don't silence exceptions without good reason
"""
print(best_practices)
