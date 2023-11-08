#!/usr/bin/python3


class MyClass:
    pass


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
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute_name] = attribute_value
