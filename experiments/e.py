# !/usr/bin/env python3
"""e.py

Python file with many different docstring styles and formats.

"""

# =============================================================================
# 1. ONE-LINE DOCSTRING (PEP 257)
# =============================================================================
# DESCRIPTION:
#   The simplest form of docstring - a single line enclosed in triple quotes.
#   It should fit on one line and end with a period. The closing quotes are
#   on the same line as the opening quotes.
#
# WHAT IT DOES:
#   Provides a brief, concise description of what the function/class does.
#   Should be a phrase ending in a period, written as a command (e.g.,
#   "Return the sum" not "Returns the sum").
#
# WHY USE IT:
#   - Perfect for simple, self-explanatory functions
#   - Minimal overhead for straightforward code
#   - Follows Python's official style guide (PEP 257)
#   - Quick to write and easy to read
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   Universal standard for simple functions. Every Python developer uses this.
#   It's the baseline that all other styles build upon.
# =============================================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


# =============================================================================
# 2. MULTI-LINE DOCSTRING (PEP 257)
# =============================================================================
# DESCRIPTION:
#   An extended docstring that spans multiple lines. The first line is a
#   summary, followed by a blank line, then a more detailed description.
#   The closing quotes are on their own line.
#
# WHAT IT DOES:
#   Provides both a quick summary and detailed explanation. The summary line
#   can be used by automatic indexing tools, while the detailed description
#   gives developers more context.
#
# WHY USE IT:
#   - When a one-liner isn't enough to explain the function
#   - To provide context, caveats, or implementation details
#   - Still follows PEP 257 without committing to a specific format style
#   - Good for internal documentation without formal structure
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   Standard approach when more detail is needed. Used everywhere in Python.
#   Forms the foundation that Google, NumPy, and other styles extend.
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
# DESCRIPTION:
#   Developed by Google, this style uses indented sections with headers like
#   Args, Returns, Raises, Examples, etc. Each section uses a specific format
#   with parameter names followed by types in parentheses and descriptions.
#
# WHAT IT DOES:
#   Organizes documentation into clear, scannable sections. Makes it easy to
#   quickly find parameter info, return values, and exceptions. The format is
#   human-readable while still being parseable by documentation generators.
#
# WHY USE IT:
#   - Extremely readable in source code (clean, not cluttered)
#   - Well-supported by Sphinx (via napoleon extension) and other doc tools
#   - Great balance between detail and brevity
#   - Industry standard at many tech companies
#   - IDE support for autocompletion and tooltips
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   One of the TWO most popular styles (along with NumPy). Widely adopted in
#   industry, open-source projects, and recommended by many style guides.
#   Used by Google, TensorFlow, Keras, and countless other projects.
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
# DESCRIPTION:
#   Originated from the NumPy and SciPy projects. Uses section headers with
#   underlines (like reStructuredText) and a specific format for parameters.
#   More verbose than Google style but provides more structured detail.
#
# WHAT IT DOES:
#   Provides comprehensive documentation with clear visual separation between
#   sections. Parameters are listed with name, type, and description on
#   separate lines. Includes special sections like See Also, Notes, References.
#
# WHY USE IT:
#   - Ideal for scientific/mathematical code with complex parameters
#   - Great for documenting array shapes, dtypes, and mathematical operations
#   - Excellent for API documentation with cross-references
#   - Supported by Sphinx (via napoleon extension)
#   - Standard in the scientific Python ecosystem
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   THE standard for scientific Python. Used by NumPy, SciPy, Pandas,
#   Matplotlib, scikit-learn, and virtually all data science libraries.
#   If you're doing data science or scientific computing, use this style.
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
# DESCRIPTION:
#   Uses reStructuredText (reST) markup with field lists. Parameters are
#   documented using :param:, :type:, :returns:, :rtype:, :raises: directives.
#   This is Sphinx's native format before the napoleon extension existed.
#
# WHAT IT DOES:
#   Provides machine-parseable documentation that Sphinx can directly convert
#   to HTML, PDF, or other formats. Supports cross-referencing, links, and
#   rich formatting like notes, warnings, and code blocks.
#
# WHY USE IT:
#   - Native Sphinx support (no extensions needed)
#   - Powerful cross-referencing capabilities (:func:, :class:, :mod:)
#   - Rich formatting options (notes, warnings, code blocks, math)
#   - Good for projects heavily invested in Sphinx documentation
#   - Precise control over generated documentation
#
# POPULARITY: ⭐⭐⭐ (Moderate)
#   Was more popular before Google/NumPy styles gained traction. Still used
#   in many older projects and by developers who prefer explicit reST markup.
#   Considered more verbose and harder to read in source code than alternatives.
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
# DESCRIPTION:
#   A legacy format from the Epydoc documentation generator. Uses @-prefixed
#   tags similar to Javadoc. Includes tags like @param, @type, @return, @rtype,
#   @raise, and many metadata tags like @author, @version, @since.
#
# WHAT IT DOES:
#   Documents code using a tag-based system familiar to Java developers.
#   Provides extensive metadata capabilities for authorship, versioning,
#   licensing, and other project information within docstrings.
#
# WHY USE IT:
#   - Familiar to developers coming from Java/Javadoc
#   - Rich metadata support (@author, @version, @since, @license)
#   - Clear, explicit tag-based structure
#   - Good for projects requiring detailed attribution
#
# POPULARITY: ⭐⭐ (Low - Legacy)
#   Epydoc is no longer actively maintained (last release 2008). This style
#   is considered DEPRECATED in favor of Google or NumPy styles. You may
#   encounter it in older codebases, but avoid using it for new projects.
#   Included here for historical reference and legacy code maintenance.
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
# DESCRIPTION:
#   Applying Google style to class documentation. The class docstring describes
#   the class purpose and lists Attributes. The __init__ method gets its own
#   docstring with Args. Each method is documented individually.
#
# WHAT IT DOES:
#   Provides a complete picture of the class: what it represents, what
#   attributes it has, and how to use it. Separates class-level documentation
#   from constructor and method documentation.
#
# WHY USE IT:
#   - Clear separation between class purpose and implementation details
#   - Attributes section shows the class's state at a glance
#   - Consistent with Google style used for functions
#   - Works well with IDE tooltips and documentation generators
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   Standard approach for class documentation in Google-style projects.
#   Recommended when your project uses Google style for functions.
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
# DESCRIPTION:
#   Applying NumPy style to class documentation. Includes Parameters (for
#   __init__), Attributes, and Methods sections. More verbose but provides
#   a complete API reference in the docstring itself.
#
# WHAT IT DOES:
#   Creates a mini API reference within the class docstring. The Methods
#   section provides a quick overview of available functionality without
#   reading each method's individual docstring.
#
# WHY USE IT:
#   - Comprehensive class overview in one place
#   - Methods section acts as a quick reference guide
#   - Consistent with NumPy style used for functions
#   - Ideal for data structures and scientific computing classes
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High)
#   Standard for scientific Python classes. Used throughout NumPy, Pandas,
#   and scikit-learn. Recommended for data science projects.
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
# DESCRIPTION:
#   The docstring at the very top of a Python file (after shebang and encoding
#   declarations). Documents the entire module's purpose, contents, and usage.
#   Should be the first statement in the module.
#
# WHAT IT DOES:
#   Provides high-level documentation visible via help(module) and in generated
#   docs. Lists the module's public API (functions, classes, constants) and
#   gives usage examples for the module as a whole.
#
# WHY USE IT:
#   - First thing developers see when reading or importing your module
#   - Accessible via help() and __doc__ attribute
#   - Essential for library/package documentation
#   - Helps users understand module purpose without reading all the code
#   - Required for proper Sphinx documentation generation
#
# POPULARITY: ⭐⭐⭐⭐⭐ (Very High - Essential)
#   Every well-documented Python module should have one. It's a fundamental
#   part of Python documentation standards. Often overlooked in tutorials
#   but critical for professional and library code.
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
# DESCRIPTION:
#   Documentation for generator functions (using yield). The key difference
#   from regular functions is the use of "Yields" instead of "Returns" to
#   describe what each iteration produces.
#
# WHAT IT DOES:
#   Clarifies that the function is a generator (not a regular function) and
#   documents what values are yielded during iteration. Users understand they
#   need to iterate over the result rather than use it directly.
#
# WHY USE IT:
#   - Makes it immediately clear the function is a generator
#   - "Yields" section distinguishes from regular "Returns"
#   - Helps users understand the iteration behavior
#   - Documents the type and meaning of yielded values
#
# POPULARITY: ⭐⭐⭐⭐ (High)
#   Standard practice for generator documentation. Both Google and NumPy
#   styles support "Yields" sections. Essential when writing generators
#   to avoid confusion with regular functions.
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
# DESCRIPTION:
#   Documentation for async/await coroutine functions. The docstring format
#   is the same as regular functions, but should clarify async behavior,
#   await requirements, and any concurrency considerations.
#
# WHAT IT DOES:
#   Documents coroutines with emphasis on async-specific details: what needs
#   to be awaited, potential blocking operations, timeout handling, and how
#   to properly call the function (asyncio.run, await, etc.).
#
# WHY USE IT:
#   - Clarifies the function must be awaited
#   - Documents async-specific exceptions (TimeoutError, CancelledError)
#   - Shows proper usage with asyncio
#   - Warns about blocking operations or concurrency issues
#
# POPULARITY: ⭐⭐⭐⭐ (High - Growing)
#   Increasingly important as async Python becomes more common. Standard
#   docstring styles (Google, NumPy) work well for async functions with
#   minor additions for async-specific details.
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
# DESCRIPTION:
#   Documentation for @property decorated methods. Properties look like
#   attributes but are actually methods, so they need documentation explaining
#   their behavior, especially if they have setters with validation.
#
# WHAT IT DOES:
#   Documents what the property returns, any side effects of getting/setting,
#   validation rules for setters, and exceptions that might be raised.
#   The format "type: Description" on the first line is common for properties.
#
# WHY USE IT:
#   - Properties can have complex behavior that needs explanation
#   - Setter validation rules should be documented
#   - Users need to know if getting a property has side effects
#   - Computed properties may need performance notes
#
# POPULARITY: ⭐⭐⭐⭐ (High)
#   Important for any class using properties. The compact "type: Description"
#   format is recommended by Google style for simple properties. More complex
#   properties use full docstring format with Raises section.
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
# DESCRIPTION:
#   Documentation for decorator functions. Decorators modify other functions,
#   so the docstring must explain what transformation occurs and how the
#   decorated function's behavior changes.
#
# WHAT IT DOES:
#   Explains what the decorator adds to or changes about the wrapped function.
#   Documents the expected signature of functions it can decorate, any new
#   attributes or methods added, and whether it preserves the original
#   function's metadata (via @functools.wraps).
#
# WHY USE IT:
#   - Decorators are "magic" that needs explanation
#   - Users need to understand how their function will be modified
#   - Important to document if decorator changes function signature
#   - Should clarify if it works with methods, classes, or both
#
# POPULARITY: ⭐⭐⭐⭐ (High)
#   Essential for any reusable decorator. Good decorator documentation
#   shows before/after examples to illustrate the transformation.
#   Both Google and NumPy styles work well for decorator documentation.
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
# DESCRIPTION:
#   Documentation for context managers (classes with __enter__/__exit__ or
#   functions using @contextmanager). Must explain the resource lifecycle:
#   what happens on entry, what's returned, and cleanup on exit.
#
# WHAT IT DOES:
#   Documents the "with" statement behavior: resource acquisition, the
#   object returned by __enter__ (the "as" value), cleanup actions in
#   __exit__, and exception handling behavior.
#
# WHY USE IT:
#   - Context managers have implicit behavior that needs documentation
#   - Users need to know what "as variable" will receive
#   - Critical to document if exceptions are suppressed or re-raised
#   - Resource cleanup guarantees should be clearly stated
#
# POPULARITY: ⭐⭐⭐⭐ (High)
#   Essential for any context manager. The pattern is widely used for
#   file handling, database connections, locks, and resource management.
#   Good documentation prevents resource leaks and misuse.
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
