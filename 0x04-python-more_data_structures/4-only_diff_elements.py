#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Returns a set of all elements presentin  one set.'''
    return not (set_1 ^ set_2)
