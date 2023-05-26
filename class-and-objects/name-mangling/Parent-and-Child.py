#!/usr/local/bin/python3

class Parent:
    def __init__(self):
        pass

    def display(self):
        print("This is printed from the Parent class")

    __display = display


class Child(Parent):
    def display(self):
        print("This is printed from the child class")

    __display = display


