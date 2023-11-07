#!/usr/bin/python3
"""Define class_to_json function"""

def class_to_json(obj):
    """ retuns the dictionary description with simple data structure """

    dic = {}

    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
