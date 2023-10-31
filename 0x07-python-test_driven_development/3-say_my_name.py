#!/usr/bin/python3
""" The module of the say_my_name method."""

def say_my_name(first_name, last_name=""):
    """
    function that print full name

    Args:
        first_name: is a string type
        last_name: is a strin gtype

    Returns:
        Full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {}".format(first_name), end="")

    if first_name != "":
        print(" ", end="")
    print(last_name)
