#!/usr/bin/python3
""" lookup module """

def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object
    Args:
        obj: input object

    Return: list of object
    """
    
    # To obtain a list of attributes and methods
    attributes_methods = dir(obj)

    return attributes_methods
