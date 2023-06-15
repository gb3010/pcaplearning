#!/usr/local/bin/python3
def Div(a,b):
    try:
        c = a / b
    except TypeError:
        print("Only integers are allowed")
    else:
        print(f"The division of {a} and {b} is {c}")
    finally:
        print("Thanks for trying Div function")

x = input("Enter value 1: ")
y = input("Enter value 2: ")
Div(x,y)



