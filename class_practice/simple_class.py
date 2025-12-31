#!/usr/bin/env python3
"""simple_class.py

Simple example of a class in Python from CS50 - Lecture 8 - Object Oriented Programming.

"""


# Initializing class "Student".
class Student:
    ...


# Defining main function which carries student object initialization and
# printing of attributes.
def main():
    student = Student()
    print(f"{student.name} from {student.house}")


# Function to get student details from user input using the "Student" class,
# "student" object, and "student" attributes.

# These attributes can also be called instance variables because they are
# tied to a specific instance of the class and are variables that belong to
# that instance.

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
