#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Function that prints a dictionary by ordered keys.'''
    ordered_list = sorted(list(a_dictionary.keys()))
    for elt in ordered_list:
        print("{}: {}".format(elt, a_dictionary.get(i)))
