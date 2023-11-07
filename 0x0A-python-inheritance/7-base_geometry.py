#!/usr/bin/python3

class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """
        Method that raises an Exception indicating that
        'area()' is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method for validating an integer value.

        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the 'value' is not an integer.
            ValueError: If the 'value' is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

