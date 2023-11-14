#!/usr/bin/python3
""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.validate_positive_integer(value, "width")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.validate_positive_integer(value, "height")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.validate_non_negative_integer(value, "x")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.validate_non_negative_integer(value, "y")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = '\n' * self.y
        rectangle += (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rectangle, end='')

    def __str__(self):
        """ str special method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update method """
        if args:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, list_atr[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns a dictionary with properties """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def validate_positive_integer(self, value, attribute):
        """ Validate if a value is a positive integer """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{attribute} must be a positive integer")

    def validate_non_negative_integer(self, value, attribute):
        """ Validate if a value is a non-negative integer """
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{attribute} must be a non-negative integer")

