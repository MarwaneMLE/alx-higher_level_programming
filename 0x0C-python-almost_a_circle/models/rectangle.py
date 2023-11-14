#!/usr/bin/python3
""" Rectangle module """

# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x: x-coordinate of the rectangle (default is 0)
            y: y-coordinate of the rectangle (default is 0)
            id: If provided, assign this value to the id attribute.
                If not, increment __nb_objects and assign the new value to id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Call the constructor of the Base class with id
        super().__init__(id)


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

 
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    # Adding the public method "area"
    def area(self):
        """ Function hat return the area of Rectangle """
        return self.width * self.height

    '''def display(self):
        """ Display a rectangle with # based on the width and height"""
        for i in range(self.__height):
            for j in range(1, self.__width):
                print("#", end="")
            print("#")'''
    
    def display(self):
        """ Display a rectangle with # based on the width and height"""
        for i in range(self.y):
            print("")
        for i in range(self.__height):
            for j in range(1, self.__width):
                print("#", end="")
            print("#")

    
    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for x in args:
                if a == 0:
                    if x is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = x
                elif a == 1:
                    self.width = x
                elif a == 2:
                    self.height = x
                elif a == 3:
                    self.x = x
                elif a == 4:
                    self.y = x
                a += 1
        
        elif kwargs and len(kwargs) != 0:
            for t, s in kwargs.items():
                if t == "id":
                    if s is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = s
                elif t == "width":
                    self.width = s
                elif t == "height":
                    self.height = s
                elif t == "x":
                    self.x = s
                elif t == "y":
                    self.y = s

    # Rectangle instance to dictionary representation
    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

    def __str__(self):
        """Return humain readbale of an object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format( self.id, self.x, self.y, self.width, self.height)
