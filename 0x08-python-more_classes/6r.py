#!/usr/bin/python3
"""
The "Rectangle" module

This module provides a Rectangle class with two attribute width and height.
And methods area, perimeter, print, str, repr, and del, and
class attribute number_of_instances that keeps track of # of instances.
"""

class Rectangle:
    """
    A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute number_of_instances that keeps track of # of instances.
    """

    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """Initializes the data """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


    @property
    def width(self):
        return self.__width


    @width.setter
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

        self.__width = value


    @property
    def height(self):
        return self.__height


    @height.setter
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

        self.__height = value


    def __repr__(self):
        """ Return a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)


    def __str__(self):
        # Initialize an empty string to build the rectangle's string repres.
        total = ""

        if self.__height == 0 or self.__width == 0:
            return total

        for i in range(self.__height):
            # Loop through each row of the rectangle
            total += ("#" * self.__width)  # Add a row of '#' characters

            if i != self.__height - 1:
                # If this is not the last row, add a newline character
                total += "\n"
        return total


    def __def__(self):
        # Custom message when an instance is deleted
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


    def area(self):
        """Function that count the area of rectangle"""
        return self.__width * self.__height


    def perimeter(self):
        """Function that Count the rectangle perimeter"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)
