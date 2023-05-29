#!/usr/local/bin/python3
class SimpleClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greet(self):
        print(f"Hello {self.name}!")

    def __str__(self):  # String representation of an object
        return f"The first name is {self.fname} and the last name is {self.lname}"

