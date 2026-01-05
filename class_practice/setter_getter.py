#!/usr/bin/env python3
"""setter_getter.py

A setter and getter practice module in classes for demonstration purposes.

"""


class Person:
    """A simple class to demonstrate getters and setters."""

    def __init__(self, name):
        self._name = name  # Private attribute (by convention)

    # Getter - retrieves the value
    @property
    def name(self):
        return self._name

    # Setter - sets/updates the value
    @name.setter
    def name(self, value):
        self._name = value


# Demo
if __name__ == "__main__":
    person = Person("Alice")

    # Using getter
    print(f"Name: {person.name}")

    # Using setter
    person.name = "Bob"
    print(f"Updated name: {person.name}")
