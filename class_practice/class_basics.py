#!/usr/bin/env python3
"""class_basics.py - A beginner's guide to Python classes"""

# =============================================================================
# LESSON 1: What is a Class?
# =============================================================================
# A class is like a blueprint for creating objects.
# Think of it like a cookie cutter - the class is the cutter,
# and each cookie you make is an "object" or "instance".


# =============================================================================
# LESSON 2: Creating Your First Class
# =============================================================================
class Dog:
    """A simple Dog class to demonstrate basic concepts."""
    
    # The __init__ method is called when you create a new Dog
    # "self" refers to the specific dog being created
    def __init__(self, name, age):
        self.name = name  # This is an "attribute" - data stored in the object
        self.age = age
    
    # This is a "method" - a function that belongs to the class
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def describe(self):
        print(f"{self.name} is {self.age} years old.")


# =============================================================================
# LESSON 3: Creating Objects (Instances)
# =============================================================================
# Let's create some dogs!

my_dog = Dog("Buddy", 3)      # Create a Dog named Buddy, age 3
your_dog = Dog("Max", 5)      # Create another Dog named Max, age 5

# Each dog is its own separate object with its own data
print("--- Accessing Attributes ---")
print(f"My dog's name: {my_dog.name}")
print(f"Your dog's name: {your_dog.name}")

print("\n--- Calling Methods ---")
my_dog.bark()        # Buddy says: Woof!
your_dog.bark()      # Max says: Woof!

my_dog.describe()    # Buddy is 3 years old.
your_dog.describe()  # Max is 5 years old.


# =============================================================================
# LESSON 4: Try It Yourself!
# =============================================================================
# Create your own simple class below. Here's a starter:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        print(f"'{self.title}' by {self.author}")


# Create a book and call its method
my_book = Book("Python Basics", "John Smith")
print("\n--- Your Book ---")
my_book.info()


# =============================================================================
# KEY TAKEAWAYS:
# =============================================================================
# 1. class ClassName:     -> Defines a new class
# 2. __init__(self, ...): -> Runs when creating a new object
# 3. self.attribute       -> Stores data in the object
# 4. def method(self):    -> Creates a function for the class
# 5. object = ClassName() -> Creates a new instance
# =============================================================================
