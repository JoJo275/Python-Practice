"""e4.py

Python file demonstrating advanced type hinting features and docstring conventions.

"""

from typing import (
    List,
    Dict,
    Optional,
    Union,
    Tuple,
    Callable,
    TypeVar,
    Generic,
    Literal,
)
from dataclasses import dataclass


# Type Variables for generics
T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def greet(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The name of the person to greet.

    Returns:
        A personalized greeting string.

    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def process_items(items: List[int], multiplier: float = 1.0) -> List[float]:
    """Process a list of integers by applying a multiplier.

    Args:
        items: A list of integers to process.
        multiplier: The value to multiply each item by. Defaults to 1.0.

    Returns:
        A list of floats representing the processed items.

    Raises:
        ValueError: If the multiplier is negative.
    """
    if multiplier < 0:
        raise ValueError("Multiplier cannot be negative")
    return [item * multiplier for item in items]


def find_user(
    users: Dict[str, int], user_id: str
) -> Optional[int]:
    """Find a user's age by their ID.

    Args:
        users: A dictionary mapping user IDs to ages.
        user_id: The ID of the user to find.

    Returns:
        The user's age if found, None otherwise.
    """
    return users.get(user_id)


def parse_input(value: Union[str, int, float]) -> str:
    """Convert various input types to a string representation.

    Args:
        value: The input value which can be a string, integer, or float.

    Returns:
        A string representation of the input value.
    """
    return str(value)


def get_coordinates() -> Tuple[float, float, float]:
    """Return 3D coordinates as a tuple.

    Returns:
        A tuple containing (x, y, z) coordinates.
    """
    return (0.0, 0.0, 0.0)


def apply_operation(
    data: List[T], operation: Callable[[T], T]
) -> List[T]:
    """Apply an operation to each element in a list.

    Args:
        data: A list of elements of type T.
        operation: A callable that takes type T and returns type T.

    Returns:
        A new list with the operation applied to each element.
    """
    return [operation(item) for item in data]


def get_status(code: int) -> Literal["success", "error", "pending"]:
    """Get status string based on status code.

    Args:
        code: The status code (0=success, 1=error, other=pending).

    Returns:
        A literal string: 'success', 'error', or 'pending'.
    """
    if code == 0:
        return "success"
    elif code == 1:
        return "error"
    return "pending"


class Stack(Generic[T]):
    """A generic stack implementation.

    This class implements a LIFO (Last In, First Out) data structure
    that can hold elements of any type T.

    Attributes:
        _items: Internal list storing the stack elements.

    Example:
        >>> stack = Stack[int]()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
    """

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Push an item onto the stack.

        Args:
            item: The item to push onto the stack.
        """
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Remove and return the top item from the stack.

        Returns:
            The top item if the stack is not empty, None otherwise.
        """
        if self._items:
            return self._items.pop()
        return None

    def peek(self) -> Optional[T]:
        """Return the top item without removing it.

        Returns:
            The top item if the stack is not empty, None otherwise.
        """
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


@dataclass
class Point:
    """Represents a point in 2D space.

    Attributes:
        x: The x-coordinate of the point.
        y: The y-coordinate of the point.
    """

    x: float
    y: float

    def distance_from_origin(self) -> float:
        """Calculate the distance from the origin (0, 0).

        Returns:
            The Euclidean distance from the origin.
        """
        return (self.x**2 + self.y**2) ** 0.5


if __name__ == "__main__":
    # Demo usage
    print(greet("World"))
    print(process_items([1, 2, 3], 2.5))
    print(find_user({"alice": 30, "bob": 25}, "alice"))
    print(get_status(0))

    stack: Stack[str] = Stack()
    stack.push("first")
    stack.push("second")
    print(f"Popped: {stack.pop()}")

    point = Point(3.0, 4.0)
    print(f"Distance from origin: {point.distance_from_origin()}")
