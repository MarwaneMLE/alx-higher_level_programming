#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class Square inherit from Rectangle """
   
    def __init__(self, size, x=0, y=0, id=None):
        """initialize new Square
        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): The identity of the new Square. 
        """
        # super to call super Class
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the square."""
        return self.width 
    
    @size.setter
    def size(self, value):
        """ Set same value to width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for x in args:
                if a == 0:
                    if x is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = x
                elif a == 1:
                    self.size = x 
                elif a == 2:
                    self.x = x
                elif a == 3:
                    self.y = x
                a += 1
        
        elif kwargs and len(kwargs) != 0:
            for t, s in kwargs.items():
                if t == "id":
                    if s is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = s
                elif t == "size":
                    self.size = s 
                elif t == "x":
                    self.x = s
                elif t == "y":
                    self.y = s 
                    

    # Square instance to dictionary representation
    def to_dictionary(self):
        """Return the dictionary representation of a Saquare"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size, 
            "y": self.y
        }


    def __str__(self):
        """Return humain readbale of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
     
