#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Function that prints all integers of a list'''
    for i in my_list:
        if isinstance(i, int):
            print("{:d}".format(i))
