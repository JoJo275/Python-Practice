# !/usr/bin/env python3
"""e.py

Python file with many different docstring styles and formats.

"""

# =============================================================================
# 1. ONE-LINE DOCSTRING (PEP 257)
# =============================================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


# =============================================================================
# 2. MULTI-LINE DOCSTRING (PEP 257)
# =============================================================================

def multiply(a, b):
    """
    Multiply two numbers together.

    This function takes two numeric values and returns their product.
    It works with integers, floats, and complex numbers.
    """
    return a * b


# =============================================================================
# 3. GOOGLE STYLE DOCSTRING
# =============================================================================

def google_style(param1, param2, param3=None):
    """Summary line describing the function.

    Extended description of the function. Can span multiple lines
    and provide additional context about the function's behavior.

    Args:
        param1 (int): The first parameter. Description of what it does.
        param2 (str): The second parameter. Another description here.
        param3 (list, optional): The third parameter. Defaults to None.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: If param1 is negative.
        TypeError: If param2 is not a string.

    Examples:
        >>> google_style(1, "hello")
        True
        >>> google_style(2, "world", [1, 2, 3])
        True

    Note:
        This is an additional note about the function.

    Warning:
        Be careful when using this function with large inputs.
    """
    return True


# =============================================================================
# 4. NUMPY/SCIPY STYLE DOCSTRING
# =============================================================================

def numpy_style(arr, axis=None, keepdims=False):
    """
    Compute the sum of array elements over a given axis.

    Parameters
    ----------
    arr : array_like
        Input array containing elements to sum.
    axis : None or int or tuple of ints, optional
        Axis or axes along which a sum is performed.
        The default, axis=None, will sum all elements.
    keepdims : bool, optional
        If True, the axes which are reduced are left in the result
        as dimensions with size one. Default is False.

    Returns
    -------
    sum_along_axis : ndarray
        An array with the same shape as `arr`, with the specified
        axis removed.

    Raises
    ------
    ValueError
        If the axis is out of bounds for the array dimensions.
    TypeError
        If the input is not array-like.

    See Also
    --------
    numpy.mean : Compute the arithmetic mean.
    numpy.cumsum : Cumulative sum of elements.

    Notes
    -----
    Arithmetic is modular when using integer types, and no error is
    raised on overflow.

    References
    ----------
    .. [1] NumPy Documentation, "numpy.sum",
           https://numpy.org/doc/stable/reference/generated/numpy.sum.html

    Examples
    --------
    >>> numpy_style([1, 2, 3])
    6
    >>> numpy_style([[1, 2], [3, 4]], axis=0)
    array([4, 6])
    """
    return sum(arr)


# =============================================================================
# 5. RESTRUCTUREDTEXT (SPHINX) STYLE DOCSTRING
# =============================================================================

def sphinx_style(name, age, email=None):
    """
    Create a new user profile with the given information.

    This function creates and returns a dictionary containing
    user profile information.

    :param name: The user's full name.
    :type name: str
    :param age: The user's age in years.
    :type age: int
    :param email: The user's email address, defaults to None.
    :type email: str, optional
    :raises ValueError: If age is negative.
    :raises TypeError: If name is not a string.
    :returns: A dictionary containing the user profile.
    :rtype: dict

    :Example:

    >>> sphinx_style("John Doe", 30)
    {'name': 'John Doe', 'age': 30, 'email': None}

    .. note::
        Email validation is not performed by this function.

    .. warning::
        Personal data should be handled according to privacy regulations.

    .. seealso::
        :func:`update_user`, :func:`delete_user`
    """
    return {"name": name, "age": age, "email": email}


# =============================================================================
# 6. EPYTEXT STYLE DOCSTRING (Epydoc)
# =============================================================================

def epytext_style(x, y):
    """
    Calculate the distance between two points.

    @param x: The x-coordinate of the point.
    @type x: float
    @param y: The y-coordinate of the point.
    @type y: float
    @return: The Euclidean distance from the origin.
    @rtype: float
    @raise ValueError: If coordinates are not numeric.

    @note: This calculates distance from the origin (0, 0).
    @attention: Coordinates must be numeric values.
    @bug: Does not handle complex numbers.
    @version: 1.0
    @since: 2024-01-01
    @author: Developer Name
    @copyright: 2024 Company Name
    @license: MIT
    @contact: dev@example.com
    """
    return (x**2 + y**2) ** 0.5


# =============================================================================
# 7. CLASS DOCSTRING (Google Style)
# =============================================================================

class GoogleStyleClass:
    """A sample class demonstrating Google-style docstrings.

    This class provides an example of how to document a Python class
    using the Google docstring format.

    Attributes:
        name (str): The name of the instance.
        value (int): A numeric value associated with the instance.
        _private (list): A private list for internal use.

    Example:
        >>> obj = GoogleStyleClass("test", 42)
        >>> obj.name
        'test'
    """

    def __init__(self, name, value):
        """Initialize the GoogleStyleClass.

        Args:
            name (str): The name to assign to this instance.
            value (int): The initial value.
        """
        self.name = name
        self.value = value
        self._private = []

    def process(self, data):
        """Process the input data.

        Args:
            data (list): A list of items to process.

        Returns:
            list: The processed data.

        Raises:
            ValueError: If data is empty.
        """
        if not data:
            raise ValueError("Data cannot be empty")
        return [item * self.value for item in data]


# =============================================================================
# 8. CLASS DOCSTRING (NumPy Style)
# =============================================================================

class NumpyStyleClass:
    """
    A sample class demonstrating NumPy-style docstrings.

    This class provides an example of how to document a Python class
    using the NumPy/SciPy docstring format.

    Parameters
    ----------
    name : str
        The name of the instance.
    value : int
        A numeric value associated with the instance.

    Attributes
    ----------
    name : str
        The name of the instance.
    value : int
        A numeric value associated with the instance.
    history : list
        A list tracking all operations performed.

    Methods
    -------
    compute(x, y)
        Compute a result based on x and y values.
    reset()
        Reset the instance to its initial state.

    Examples
    --------
    >>> obj = NumpyStyleClass("example", 10)
    >>> obj.compute(2, 3)
    50
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.history = []


# =============================================================================
# 9. MODULE-LEVEL DOCSTRING EXAMPLE
# =============================================================================

MODULE_DOCSTRING_EXAMPLE = '''
"""
Module Name
===========

Short description of the module.

This module provides utilities for [purpose]. It includes functions
for [functionality 1], [functionality 2], and [functionality 3].

Functions
---------
function_one(arg1, arg2)
    Description of function one.
function_two(arg1)
    Description of function two.

Classes
-------
ClassName
    Description of the class.

Constants
---------
CONSTANT_NAME : type
    Description of the constant.

Examples
--------
>>> import module_name
>>> module_name.function_one(1, 2)
3

Notes
-----
Additional notes about the module.

See Also
--------
related_module : Description of related module.

References
----------
.. [1] Reference to relevant documentation or paper.

"""
'''


# =============================================================================
# 10. GENERATOR FUNCTION DOCSTRING
# =============================================================================

def generator_docstring(n):
    """
    Generate a sequence of Fibonacci numbers.

    This generator yields Fibonacci numbers up to the nth term.

    Args:
        n (int): The number of Fibonacci terms to generate.

    Yields:
        int: The next Fibonacci number in the sequence.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> list(generator_docstring(5))
        [0, 1, 1, 2, 3]

    Note:
        This is a generator function and must be iterated over.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# =============================================================================
# 11. ASYNC FUNCTION DOCSTRING
# =============================================================================

async def async_docstring(url, timeout=30):
    """
    Fetch data from a URL asynchronously.

    This coroutine fetches data from the specified URL with
    configurable timeout.

    Args:
        url (str): The URL to fetch data from.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.

    Returns:
        dict: The JSON response parsed as a dictionary.

    Raises:
        TimeoutError: If the request exceeds the timeout.
        ConnectionError: If unable to connect to the URL.

    Examples:
        >>> import asyncio
        >>> data = asyncio.run(async_docstring("https://api.example.com"))

    Warning:
        Ensure proper exception handling when using in production.
    """
    pass  # Implementation would go here


# =============================================================================
# 12. PROPERTY DOCSTRING
# =============================================================================

class PropertyDocstring:
    """Class demonstrating property docstrings."""

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """int: The current value.

        This property returns the internal value. Setting this property
        will validate that the new value is positive.

        Raises:
            ValueError: If attempting to set a negative value.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value


# =============================================================================
# 13. DECORATOR DOCSTRING
# =============================================================================

def decorator_docstring(func):
    """
    A decorator that logs function calls.

    This decorator wraps a function and logs its name and arguments
    each time it is called.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with logging capability.

    Examples:
        >>> @decorator_docstring
        ... def my_function(x):
        ...     return x * 2
        >>> my_function(5)
        Calling my_function with args: (5,)
        10
    """
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        return func(*args, **kwargs)
    return wrapper


# =============================================================================
# 14. CONTEXT MANAGER DOCSTRING
# =============================================================================

class ContextManagerDocstring:
    """
    A context manager for managing resources.

    This context manager handles resource acquisition and cleanup
    automatically using the with statement.

    Args:
        resource_name (str): The name of the resource to manage.

    Attributes:
        resource_name (str): The name of the managed resource.
        is_open (bool): Whether the resource is currently open.

    Examples:
        >>> with ContextManagerDocstring("database") as cm:
        ...     print(cm.is_open)
        True

    Note:
        Resources are automatically cleaned up when exiting the context.
    """

    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.is_open = False

    def __enter__(self):
        """Enter the context and acquire the resource."""
        self.is_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context and release the resource."""
        self.is_open = False
        return False
