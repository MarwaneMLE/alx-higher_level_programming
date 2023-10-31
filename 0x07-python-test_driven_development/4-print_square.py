#!/usr/bin/python3
def print_square(size):
    """ Function that prints a square with the character #.
    Args:
        size: the size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    if size > 0:
        for i in range(size):
            print("#" * size)
    else:
        # If size is 0, nothing is printed
        print("")
