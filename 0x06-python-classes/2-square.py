#!/usr/bin/python3
class Square:
    """ Class to count square of given number """
    def __init__(self, size=0):
        self.size =  size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def square(self):
        return self.size ** 2 
