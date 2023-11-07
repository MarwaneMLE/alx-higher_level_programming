#!/usr/bin/python3
"""MyList Module"""

class MyList(list):
    """ MyList class that inherits from list"""
    def print_sorted(self):
        """ Function that prints sorted list"""
        sorted_list = sorted(self)
        print(sorted(sorted_list))
