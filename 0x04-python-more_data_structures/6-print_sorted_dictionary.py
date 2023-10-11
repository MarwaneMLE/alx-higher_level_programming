#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Function that prints a dictionary by ordered keys.'''
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for elt in ordered_list:
        print("{}: {}".format(elt, a_dictionary.get(i)))
