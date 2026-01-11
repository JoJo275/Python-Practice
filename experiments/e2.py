"""e2.py


This module demonstrates various docstring conventions including:
- Module-level docstrings
- Function docstrings (Google, NumPy, and reStructuredText styles)
- Class docstrings
- Method docstrings

Author: ID136
Date: 2026-01-11

maybe code different type hints in future

"""


# =============================================================================
# Google Style Docstrings
# =============================================================================

def google_style_example(param1: str, param2: int, param3: list = None) -> dict:
    """Short summary of the function.

    Longer description of the function that can span multiple lines
    and provides more detail about what the function does.

    Args:
        param1: The first parameter description.
        param2: The second parameter description.
        param3: Optional; defaults to None. A list of values.

    Returns:
        A dictionary containing the processed results with keys:
            - 'status': Success or failure indicator
            - 'data': The processed data

    Raises:
        ValueError: If param1 is empty.
        TypeError: If param2 is not an integer.

    Example:
        >>> result = google_style_example("test", 42)
        >>> print(result)
        {'status': 'success', 'data': 'test-42'}
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    if not isinstance(param2, int):
        raise TypeError("param2 must be an integer")

    return {"status": "success", "data": f"{param1}-{param2}"}


# =============================================================================
# NumPy Style Docstrings
# =============================================================================

def numpy_style_example(array: list, multiplier: float = 1.0) -> list:
    """
    Multiply each element in an array by a given multiplier.

    This function takes a list of numbers and multiplies each element
    by the specified multiplier value.

    Parameters
    ----------
    array : list
        A list of numeric values to be multiplied.
    multiplier : float, optional
        The value to multiply each element by (default is 1.0).

    Returns
    -------
    list
        A new list with each element multiplied by the multiplier.

    Raises
    ------
    TypeError
        If array is not a list or multiplier is not numeric.

    See Also
    --------
    google_style_example : Example using Google style docstrings.

    Notes
    -----
    This function creates a new list and does not modify the original.

    Examples
    --------
    >>> numpy_style_example([1, 2, 3], 2.0)
    [2.0, 4.0, 6.0]

    >>> numpy_style_example([10, 20], 0.5)
    [5.0, 10.0]
    """
    return [element * multiplier for element in array]


# =============================================================================
# reStructuredText (Sphinx) Style Docstrings
# =============================================================================

def rst_style_example(text: str, repeat: int = 1) -> str:
    """
    Repeat a text string a specified number of times.

    :param text: The text string to repeat.
    :type text: str
    :param repeat: Number of times to repeat the text, defaults to 1.
    :type repeat: int, optional
    :returns: The repeated text joined by spaces.
    :rtype: str
    :raises ValueError: If repeat is less than 1.

    :Example:

    >>> rst_style_example("hello", 3)
    'hello hello hello'

    .. note::
        The repeated strings are joined with single spaces.

    .. warning::
        Large repeat values may consume significant memory.
    """
    if repeat < 1:
        raise ValueError("repeat must be at least 1")
    return " ".join([text] * repeat)


# =============================================================================
# Class Docstring Example
# =============================================================================

class DocumentedClass:
    """
    A well-documented example class demonstrating docstring conventions.

    This class serves as an example of how to properly document a Python
    class including its attributes, methods, and special behaviors.

    Attributes:
        name (str): The name identifier for this instance.
        value (int): A numeric value associated with this instance.
        _internal (list): Private list for internal storage.

    Example:
        >>> obj = DocumentedClass("example", 100)
        >>> obj.name
        'example'
        >>> obj.describe()
        'DocumentedClass: example with value 100'
    """

    def __init__(self, name: str, value: int = 0):
        """
        Initialize a new DocumentedClass instance.

        Args:
            name: The name identifier for this instance.
            value: Initial numeric value (default: 0).
        """
        self.name = name
        self.value = value
        self._internal = []

    def describe(self) -> str:
        """
        Return a human-readable description of this instance.

        Returns:
            A formatted string describing the instance.
        """
        return f"DocumentedClass: {self.name} with value {self.value}"

    def add_item(self, item) -> None:
        """
        Add an item to the internal storage.

        Args:
            item: Any object to add to internal storage.

        Note:
            Items are stored in insertion order.
        """
        self._internal.append(item)

    @property
    def item_count(self) -> int:
        """int: The number of items in internal storage."""
        return len(self._internal)


# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    # Demonstrate Google style function
    print("Google Style Example:")
    result = google_style_example("test", 42)
    print(f"  Result: {result}\n")

    # Demonstrate NumPy style function
    print("NumPy Style Example:")
    result = numpy_style_example([1, 2, 3, 4, 5], 2.0)
    print(f"  Result: {result}\n")

    # Demonstrate RST style function
    print("RST Style Example:")
    result = rst_style_example("Python", 3)
    print(f"  Result: {result}\n")

    # Demonstrate class usage
    print("Class Example:")
    obj = DocumentedClass("demo", 50)
    obj.add_item("first")
    obj.add_item("second")
    print(f"  Description: {obj.describe()}")
    print(f"  Item count: {obj.item_count}")
