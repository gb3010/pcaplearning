#!/usr/bin/python3
def Divide(a,b):
    try:
        x = a / b
    except ZeroDivisionError:
        if b == 0:
            print("Cannot divide by zero!")


Divide(2,0)