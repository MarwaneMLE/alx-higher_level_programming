#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    Add a new attribute to an object if it's possible; otherwise, raise a TypeError.
    Args:
        obj: The object to which the attribute will be added.
        attribute_name: The name of the attribute.
        attribute_value: The value of the attribute.
    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")
