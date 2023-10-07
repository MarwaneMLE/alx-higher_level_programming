#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that retrieves an element from a list"""
    if idx < 0:
       print("{}".format(None))
    elif idx > len(my_list):
        print("{}".format(None))
    else:
        element = my_list[idx]
        print("Element at index {:d} is {}".format(idx, element))
