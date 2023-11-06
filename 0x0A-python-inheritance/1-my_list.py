#!/usr/bin/python3
""" Class MyList inherit from list """

class MyList(list):
    def print_sorted(self):
        """ Function that prints the list, but sorted (ascending sort) """
        sorted_list = sorted(self)
        print(sorted(sorted_list))
