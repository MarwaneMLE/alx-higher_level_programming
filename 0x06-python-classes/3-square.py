#!/usr/bin/python3
class Square:
    """ Class to count square of given number """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size,int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
