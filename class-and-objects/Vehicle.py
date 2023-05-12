#!/usr/loca/bin/python3
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"The make is {self.make} and the model is {self.model}")
