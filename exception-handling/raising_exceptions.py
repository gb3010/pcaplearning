#!/usr/local/bin/python
def NumberCheck(x):
    if x < 0:
        raise Exception("Only positive numbers allowed") # Raising an exception within the function
    elif x == 0:
        raise Exception("Non negative number required")


a = int(input("Enter a number: "))
try:
    NumberCheck(a)
except Exception as e: # Using the exception to catch the error
    print(f"Error: {e}")
else:
    print("The input was a positive number. The number check was successful")