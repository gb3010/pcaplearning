#!/usr/local/bin/python3
class ParentClass:
    def __init__(self):
        pass

    def display(self):
        print("This is from the Parent class")


class ChildClass(ParentClass):
    def __init__(self):
        pass

    def display(self):
        print("This is from the child class")


obj1 = ChildClass()
obj1.display()
