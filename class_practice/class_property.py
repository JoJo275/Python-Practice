#! /usr/bin/env python3
"""class_property.py

Simple example of class properties in Python.

"""


class Dog:
    """A simple Dog class to demonstrate properties."""

    def __init__(self, name, age):
        """Initialize the dog with a name and age."""
        self._name = name  # The underscore means "private" (by convention)
        self._age = age

    # --- PROPERTY: A way to access private attributes safely ---

    @property
    def name(self):
        """Getter: Returns the dog's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter: Sets the dog's name (with validation)."""
        if not value:
            raise ValueError("Name cannot be empty!")
        self._name = value

    @property
    def age(self):
        """Getter: Returns the dog's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter: Sets age (only if positive number)."""
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    # --- BONUS: Read-only property (no setter) ---

    @property
    def human_years(self):
        """Calculates dog's age in human years (read-only)."""
        return self._age * 7


# --- DEMO ---
if __name__ == "__main__":
    # Create a dog
    my_dog = Dog("Buddy", 3)

    # Access properties (looks like attributes, but uses getters!)
    print(f"Name: {my_dog.name}")  # Uses @property getter
    print(f"Age: {my_dog.age}")
    print(f"Human years: {my_dog.human_years}")

    # Modify using setters
    my_dog.name = "Max"  # Uses @name.setter
    my_dog.age = 5
    print(f"\nUpdated name: {my_dog.name}")
    print(f"Updated age: {my_dog.age}")

    # Try invalid values (uncomment to test)
    # my_dog.age = -1  # Raises ValueError!
    # my_dog.name = ""  # Raises ValueError!
