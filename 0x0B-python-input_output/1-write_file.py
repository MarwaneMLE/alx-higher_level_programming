#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args:
        filename:The name of the file to write(str)
        text: The text to write to the file(str)
    Return:
        the number of characters writtrn.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
