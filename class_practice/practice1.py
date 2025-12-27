#! /usr/bin/env python3
"""practice1.py

A small but educational program teaching the basics of classes in Python.

"""


# A class is a blueprint for creating objects
class Dog:
    # __init__ is the constructor - runs when you create a new Dog
    def __init__(self, name, age):
        # 'self' refers to the instance being created
        self.name = name  # Instance attribute
        self.age = age

    # A method is a function that belongs to the class
    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."


# Main block - only runs if this file is executed directly
if __name__ == "__main__":
    # Create instances (objects) from the class
    my_dog = Dog("Buddy", 3)
    your_dog = Dog("Max", 5)

    # Call methods on the objects
    print(my_dog.bark())        # Buddy says woof!
    print(your_dog.describe())  # Max is 5 years old.
