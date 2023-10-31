class Rectangle:
    """
    Rectangle class with width, height, methods for area, perimeter, and comparison, 
    and class attributes for instance tracking and symbol for printing.
    """

    number_of_instances = 0  # Class attribute to count instances
    print_symbol = "#"  # Class attribute for the symbol used for printing

    def __init__(self, width=0, height=0):
        # Constructor to initialize the width and height attributes and increment the instance count
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Setter for width with type and value checks
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
        # Setter for height with type and value checks
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # Static method to compare two rectangles and return the bigger one
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __repr__(self):
        # String representation for recreating an instance
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        # Generate a string representation of the rectangle using print_symbol
        return "\n".join([str(self.print_symbol * self.__width) for _ in range(self.__height)]

    def __del__(self):
        # Custom message when an instance is deleted and decrement instance count
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

