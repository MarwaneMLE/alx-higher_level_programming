#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ Class to count square of given number
    Attribute:
            size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        Args:
            size: size of the square (1 side).
        """
        self.size =  size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def square(self):
        return self.size ** 2
