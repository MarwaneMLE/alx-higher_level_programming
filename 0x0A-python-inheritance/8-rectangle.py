#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Initialize private attributes
        self.__width = 0
        self.__height = 0

        # Validate width and height using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set private attributes for width and height
        self.__width = width
        self.__height = height

