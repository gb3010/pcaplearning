#!/usr/local/bin/python3
class ParentClass:
    def __init__(self):
        pass

    def display(self):
        print("This is from the Parent class")

class ParentClass2:
    def __init__(self):
        pass

    def display(self):
        print("This is from the Parent class 2")

class ChildClass(ParentClass,ParentClass2):
    def __init__(self):
        pass

    def display(self):
        print("This is from the child class")



obj1 = ChildClass()
obj1.display()
