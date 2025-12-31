#!/usr/bin/env python3
"""simple_class.py

Simple example of a class in Python from CS50 - Lecture 8 - Object Oriented Programming.

"""

class Student:
    ...

def main():
    student = Student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

