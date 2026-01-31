"""
Decorators Demystified
======================

Understanding Python decorators from basics to advanced patterns.
"""

import time
from functools import wraps

# 1. What is a Decorator?
print("=== Basic Decorator ===")

def simple_decorator(func):
    """A decorator is a function that wraps another function."""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# 2. Preserving Function Metadata with @wraps
print("\n=== Using @wraps ===")

def better_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def documented_function():
    """This docstring is preserved."""
    pass

print(f"Function name: {documented_function.__name__}")
print(f"Docstring: {documented_function.__doc__}")


# 3. Practical Example: Timer Decorator
print("\n=== Timer Decorator ===")

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done!"

result = slow_function()


# 4. Decorator with Arguments
print("\n=== Decorator with Arguments ===")

def repeat(times):
    """Decorator that repeats function execution."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()


# 5. Debug Decorator
print("\n=== Debug Decorator ===")

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(5, 3)


# 6. Validate Arguments Decorator
print("\n=== Validation Decorator ===")

def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def square_root(n):
    return n ** 0.5

print(f"sqrt(16) = {square_root(16)}")

try:
    square_root(-4)
except ValueError as e:
    print(f"Caught error: {e}")


# 7. Class-based Decorator
print("\n=== Class-based Decorator ===")

class CountCalls:
    """Decorator that counts function calls."""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()


# 8. Stacking Decorators
print("\n=== Stacking Decorators ===")

@timer
@debug
def multiply(x, y):
    return x * y

# Equivalent to: timer(debug(multiply))
multiply(4, 5)


# 9. Common Built-in Decorators
print("\n=== Built-in Decorators ===")

class MyClass:
    class_var = "I'm a class variable"
    
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        """Getter using @property"""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Setter for the property"""
        self._value = new_value
    
    @classmethod
    def class_method(cls):
        """Access class, not instance"""
        return cls.class_var
    
    @staticmethod
    def static_method(x, y):
        """No access to class or instance"""
        return x + y

obj = MyClass(10)
print(f"Property: {obj.value}")
print(f"Class method: {MyClass.class_method()}")
print(f"Static method: {MyClass.static_method(3, 4)}")


if __name__ == "__main__":
    print("\n✅ Decorators guide executed successfully!")
