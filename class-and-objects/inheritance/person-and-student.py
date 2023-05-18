class Person:
    def __init__(self, fname, lname) -> object:
        self.fname = fname
        self.lname = lname

    def greeting(self):
        print(f"Hello {self.fname} {self.lname}!")


class Student(Person):  # Inherits Person class
    def __init__(self, fname, lname, rollno, year):  # Constructor of the child class
        super().__init__(fname, lname)  # Inherits all the methods and variables of
        self.rollno = rollno
        self.year = year

    def welcome(self): # A method that belongs to Student class only
        print(f"Welcome {self.fname} {self.lname} to the academic year {self.year}!")
