#!/usr/bin/python3
""" Module for add_integer method"""

def add_integer(a, b=98):
    """
    Functionthat adds 2 integers

    >>> add_integer(1, 8)
    9
    >>> add_integer(20, -2)
    18
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be integer")

    return int(a) + int(b)
