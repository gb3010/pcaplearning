#!/usr/local/bin/python3
# Assigning a function to a variable

def shout(word):
    return word.upper()


def whisper(word):
    return word.lower()


yell = shout  # Here we have assigned the 'shout' function to the variable named 'yell'
print(yell('Hello'))