# !/usr/bin/env python3
"""property_practice.py

Property Practice Module in classes for demonstration purposes.

    """


class Person:
    """A simple class to demonstrate @property decorator."""

    def __init__(self, name, age):
        self._name = name  # underscore means "private"
        self._age = age

    # Getter - lets you READ the value
    @property
    def name(self):
        return self._name

    # Setter - lets you CHANGE the value
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value


# --- Try it out! ---
if __name__ == "__main__":
    # Create a person
    person = Person("Alice", 25)

    # Use property like a normal attribute (no parentheses!)
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")

    # Change values using the setter
    person.name = "Bob"
    person.age = 30
    print(f"\nUpdated Name: {person.name}")
    print(f"Updated Age: {person.age}")

    # Try setting invalid age
    print("\nTrying to set negative age:")
    person.age = -5
    print(f"Age is still: {person.age}")

