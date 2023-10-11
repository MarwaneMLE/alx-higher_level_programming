#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Adds all unique integers in a list (only once for each integer).'''
    unique_list = []
    for integer in my_list:
        if integer not in unique_list:
            unique_list.append(integer)
    
    sum = 0
    for x in unique_list:
        sum += x
    return sum 
