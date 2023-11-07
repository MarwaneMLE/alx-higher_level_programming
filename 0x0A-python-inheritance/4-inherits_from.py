#!/usr/bin/python3
"""Module containing inherits_from method"""

def inherits_from(obj, a_class):
    """
    Return:
        True: if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class
        False: otherwise
    """
    return issubclass(type(obj), a_class)
