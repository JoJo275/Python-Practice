"""e3.py

Python document containing different methods of type hints.

"""

from typing import List, Dict, Tuple, Optional, Union, Callable, Any, TypeVar, Generic

# =============================================================================
# Basic Type Hints
# =============================================================================

def greet(name: str) -> str:
    """Basic function with string type hints."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Function with integer type hints."""
    return a + b


def divide(a: float, b: float) -> float:
    """Function with float type hints."""
    return a / b


def is_valid(flag: bool) -> bool:
    """Function with boolean type hints."""
    return not flag


# =============================================================================
# Collection Type Hints
# =============================================================================

def sum_list(numbers: List[int]) -> int:
    """Function accepting a list of integers."""
    return sum(numbers)


def get_user(users: Dict[str, int]) -> Dict[str, int]:
    """Function accepting a dictionary."""
    return users


def get_coordinates() -> Tuple[float, float]:
    """Function returning a tuple."""
    return (10.5, 20.3)


def process_items(items: List[Tuple[str, int]]) -> None:
    """Function with nested type hints."""
    for name, value in items:
        print(f"{name}: {value}")


# =============================================================================
# Optional and Union Types
# =============================================================================

def find_user(user_id: int) -> Optional[str]:
    """Function that may return None."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


def process_value(value: Union[int, str]) -> str:
    """Function accepting multiple types."""
    return str(value)


# Python 3.10+ syntax using pipe operator
def process_value_modern(value: int | str | None) -> str:
    """Modern union syntax (Python 3.10+)."""
    return str(value) if value is not None else "None"


# =============================================================================
# Callable Type Hints
# =============================================================================

def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """Function accepting another function as parameter."""
    return operation(x, y)


def multiplier(factor: int) -> Callable[[int], int]:
    """Function returning a function."""
    def multiply(x: int) -> int:
        return x * factor
    return multiply


# =============================================================================
# TypeVar and Generics
# =============================================================================

T = TypeVar('T')


def first_element(items: List[T]) -> T:
    """Generic function using TypeVar."""
    return items[0]


def identity(value: T) -> T:
    """Generic identity function."""
    return value


class Stack(Generic[T]):
    """Generic stack class."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0


# =============================================================================
# Class Type Hints
# =============================================================================

class Person:
    """Class with type-hinted attributes and methods."""
    
    name: str
    age: int
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Person":
        """Class method with type hints."""
        return cls(data["name"], data["age"])


# =============================================================================
# Type Aliases
# =============================================================================

# Simple type alias
UserId = int
Username = str

# Complex type alias
UserDict = Dict[UserId, Username]
Coordinates = Tuple[float, float]
Matrix = List[List[int]]


def get_user_by_id(user_id: UserId, users: UserDict) -> Optional[Username]:
    """Function using type aliases."""
    return users.get(user_id)


# =============================================================================
# Literal Types (Python 3.8+)
# =============================================================================

from typing import Literal

Direction = Literal["north", "south", "east", "west"]


def move(direction: Direction) -> str:
    """Function with literal type hint."""
    return f"Moving {direction}"


# =============================================================================
# Final and ClassVar
# =============================================================================

from typing import Final, ClassVar


class Config:
    """Class demonstrating Final and ClassVar."""
    
    MAX_CONNECTIONS: Final[int] = 100  # Cannot be reassigned
    instance_count: ClassVar[int] = 0  # Class-level variable
    
    def __init__(self) -> None:
        Config.instance_count += 1


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":
    # Basic types
    print(greet("World"))
    print(add(5, 3))
    
    # Collections
    print(sum_list([1, 2, 3, 4, 5]))
    print(get_coordinates())
    
    # Optional/Union
    print(find_user(1))
    print(find_user(99))
    print(process_value(42))
    print(process_value("hello"))
    
    # Callable
    result = apply_operation(10, 5, lambda x, y: x + y)
    print(f"Operation result: {result}")
    
    double = multiplier(2)
    print(f"Double 5: {double(5)}")
    
    # Generics
    print(f"First element: {first_element([1, 2, 3])}")
    print(f"First element: {first_element(['a', 'b', 'c'])}")
    
    # Generic class
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")
    
    # Class
    person = Person("Alice", 30)
    print(person.get_info())
    
    # Type aliases
    users: UserDict = {1: "alice", 2: "bob"}
    print(get_user_by_id(1, users))
    
    # Literal
    print(move("north"))
