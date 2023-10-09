#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Replaces an element in a list at a specific indexi'''
    if idx < 0 or idx >= len(my_list):
        return my_list
    copy_list = [x for x in my_list]
    copy_list[idx] = element
    return copy_list
