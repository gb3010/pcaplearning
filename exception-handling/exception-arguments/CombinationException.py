#!/usr/local/bin/python3
class CombinationException(Exception):
    def __init__(self, value1, value2, message):
        self.value1 = value1
        self.value2 = value2
        self.message = message

