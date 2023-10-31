#!/usr/bin/python3
""" class named LockedClass with a predefined number of slots """

class LockedClass:
    """if user defined, no new items can be added to list"""
    __slots__ = ['first_name']
