#!/usr/local/bin/python3
from CombinationException import CombinationException
class EvenComboCheck:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def CheckCombo(self):
        if  ( self.input1 % 2 != 0 ) or ( self.input2 % 2 == 0):
            raise CombinationException(self)


try:
    obj = EvenComboCheck(2, 5)
except:
    CombinationException(obj.input1, obj.input2, f"Both the values {self.input1} and {self.input2} are not even numbers")
