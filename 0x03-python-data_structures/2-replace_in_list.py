#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position"""
    if idx < 0:
        print("{}".format(my_list))
    elif idx > len(my_list):
        print("{}".format(my_list))
    else:
        my_list[idx] = element
        print("{}".format(my_list))
