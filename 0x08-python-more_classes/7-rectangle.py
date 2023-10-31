class Rectangle:
    """
    A Rectangle class with attributes width and height, methods area, perimeter, print, str, repr, and del,
    and class attributes number_of_instances (keeps track of the number of instances) and print_symbol (used for printing).
    """

    number_of_instances = 0  # Class attribute to keep track of the number of instances
    print_symbol = "#"  # Class attribute used as the symbol for printing

    def __init__(self, width=0, height=0):
        # Initialize the width and height attributes, and increment number_of_instances
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for the width attribute with type and value checks
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Setter for the height attribute with type and value checks
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        # Return a string representation for recreating an instance
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        # Generate a string representation of the rectangle using print_symbol
        total = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    total += str(self.print_symbol)
                except Exception:
                    total += type(self).print_symbol
            if i is not self.__height - 1:
                total += "\n"
        return total

    def __del__(self):
        # Custom message when an instance is deleted and decrement number_of_instances
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

