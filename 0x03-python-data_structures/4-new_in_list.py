#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''unction that replaces an element in a list at a specific position without modifying the original list'''
    if idx < 0:
        print("{}".format(my_list.copy()))
    elif idx > len(my_list):
        print("{}".format(my_list.copy()))
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        print("{}".format(new_list))
        print("{}".format(my_list))
