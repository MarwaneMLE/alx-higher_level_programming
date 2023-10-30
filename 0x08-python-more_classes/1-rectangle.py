#!/usr/bin/python3
""" Module for Rectangle class """

class Rectangle:
    """  class Rectangle that defines a rectangle form"""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height


    def width(self, value):
        """
        Function that retrieve width

        Args:
            value: width of the  rectangle ans is integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return value


    def height(self, value):
        """
        Function that retrieve the height

        Args:
            value: height of the rectangle ans is integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return value
