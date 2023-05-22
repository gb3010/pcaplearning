#!/usr/local/bin/python3

class Mammal:
    def mammal_info(self):
        print("Mammals give direct birth")


class Bird:
    def bird_info(self):
        print("Birds can flap their wings")


class Bat(Mammal, Bird):
    pass


b = Bat()
b.mammal_info()
b.bird_info()

