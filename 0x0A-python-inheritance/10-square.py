# Import the Rectangle class from the 9-rectangle module
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        Initialize the Square instance with a size.
        Args:
            size (int): The size of the square's sides.
        """
        # Validate and set the size
        self.integer_validator("size", size)
        self.__size = size
        # Call the constructor of the parent class with width and height as size.
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.
        Returns
            int: The area of the square.
        """

        return self.__size ** 2
