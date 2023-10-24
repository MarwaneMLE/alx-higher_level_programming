#!/usr/bin/python3
"""Square module."""


class Square:
    """ Class that count a square of given number
    Args:
        size: length of a side of the square.
    """
    def __init__(self, size):
        """Creates new instances of square (1 side).
        Args:
            size: size of the square
        """
        self.__size = size
