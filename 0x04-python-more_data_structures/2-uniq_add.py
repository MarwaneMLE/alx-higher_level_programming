#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Adds all unique integers in a list.'''
    unique_list = set(my_list)

    sum = 0
    for x in unique_list:
        sum += x
    return sum
