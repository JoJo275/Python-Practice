#!/usr/bin/env python3
"""public_private.py

A simple example to demonstrate public and private attributes in a class.

"""


class Person:
    def __init__(self, name, age, ssn):
        self.name = name        # Public: accessible anywhere
        self._age = age         # Protected: "please don't touch" (convention only)
        self.__ssn = ssn        # Private: name-mangled by Python

    # Getter method for private attribute
    def get_ssn(self):
        return self.__ssn

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, SSN: {self.__ssn}")


# --- Demo ---
if __name__ == "__main__":
    person = Person("Alice", 30, "123-45-6789")

    # Public attribute - works fine
    print(f"Public (name): {person.name}")

    # Protected attribute - works, but you shouldn't access it directly
    print(f"Protected (_age): {person._age}")

    # Private attribute - this will cause an AttributeError!
    # print(person.__ssn)  # Uncomment to see the error

    # Correct way: use a getter method
    print(f"Private via getter: {person.get_ssn()}")

    # Python's "name mangling" - private attrs become _ClassName__attr
    # This still works but is bad practice!
    print(f"Private via mangling: {person._Person__ssn}")

    # Display all info from inside the class
    person.display_info()
