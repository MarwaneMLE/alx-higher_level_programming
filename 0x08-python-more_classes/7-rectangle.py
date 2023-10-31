class Rectangle:
    """A class for rectangles with width, height, and various methods."""

    number_of_instances = 0  # Count of instances
    print_symbol = "#"  # Symbol for printing

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with the given width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        """Return a string representation for recreating an instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """Generate a string representation of the rectangle using print_symbol."""
        return "\n".join([str(self.print_symbol * self.__width) for _ in range(self.__height)]

    def __del__(self):
        """Print a custom message when an instance is deleted and decrement the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

