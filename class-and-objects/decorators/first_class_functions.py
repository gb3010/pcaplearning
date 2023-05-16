#!/usr/local/bin/python3
# Assigning a function to a variable

def shout(word):
    return word.upper()


def whisper(word):
    return word.lower()


yell = shout  # Here we have assigned the 'shout' function to the variable named 'yell'
print(yell('Hello'))

# Pass a function as an argument to another function

def double(x):
    return x * 2

def inc(x):
    return x + 1

def func_input(func, x):
    output = func(x)
    print(output)

func_input(double(2))
func_input(inc(2))

