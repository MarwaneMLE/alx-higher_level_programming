#!/usr/bin/python3
"""Rectangle class Module"""

# Import the BaseGeometry class from the 7-base_geometry module
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """

        # Validate and set the width and height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
