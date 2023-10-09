#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Replaces an element in a list at a specific position'''
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
