#!/usr/bin/python3
class Square:
    """ class Square that defines a square"""
    def __init__(self, size = 0):
        """Creates new instances of square."""
        self.__size = size

    def area(self):
        """ Calculates the area of square."""
        return self.__size ** 2

    @property
    def size(self):
        """ Return size of square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """  prints in stdout the square with the character #:"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * (self.__size))
