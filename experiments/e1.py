"""e1.py

Python file showing different comment styles and formats in python.

"""

# =============================================================================
# 1. SINGLE-LINE COMMENTS
# =============================================================================

# This is a single-line comment
x = 10  # Inline comment after code

# Multiple single-line comments
# can be used to create
# a block of explanatory text


# =============================================================================
# 2. MULTI-LINE STRINGS AS COMMENTS (DOCSTRINGS)
# =============================================================================

"""
This is a multi-line string.
When not assigned to a variable, it acts like a comment.
Often used for longer explanations.
"""

'''
You can also use single quotes
for multi-line strings/comments.
'''


# =============================================================================
# 3. FUNCTION DOCSTRINGS
# =============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width


def greet(name):
    """Return a greeting message for the given name."""  # One-line docstring
    return f"Hello, {name}!"


# =============================================================================
# 4. CLASS DOCSTRINGS
# =============================================================================

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area."""
        return self.length * self.width

    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self.length + self.width)


# =============================================================================
# 5. MODULE-LEVEL DOCSTRING (at the top of the file)
# =============================================================================
# The docstring at the very top of this file is a module-level docstring.
# It describes the purpose of the entire module/file.


# =============================================================================
# 6. TODO, FIXME, AND OTHER SPECIAL COMMENTS
# =============================================================================

# TODO: Add more examples of comment styles
# FIXME: This function needs error handling
# NOTE: This is an important note for developers
# HACK: Temporary workaround until proper fix is implemented
# XXX: This code needs attention
# BUG: Known issue - doesn't handle negative numbers


# =============================================================================
# 7. TYPE HINTS WITH COMMENTS
# =============================================================================

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


# Type comments (older style, pre-Python 3.5)
def old_style_typed(x, y):
    # type: (int, int) -> int
    """Add two numbers using old-style type comments."""
    return x + y


# =============================================================================
# 8. SECTION DIVIDERS AND HEADERS
# =============================================================================

# --- Short divider ---

# ~~~ Alternative divider ~~~

# *** Another style ***

########################################
# Block header style
########################################


# =============================================================================
# 9. SHEBANG AND ENCODING (typically at very top of file)
# =============================================================================
# #!/usr/bin/env python3  <- Shebang line (tells OS which interpreter to use)
# -*- coding: utf-8 -*-   <- Encoding declaration


# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Test the functions and classes
    print("Area of 5x3 rectangle:", calculate_area(5, 3))
    print(greet("Python Developer"))

    rect = Rectangle(10, 5)
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")

    # Access docstrings programmatically
    print("\n--- Docstring Examples ---")
    print(f"Function docstring:\n{calculate_area.__doc__}")
    print(f"\nClass docstring:\n{Rectangle.__doc__}")