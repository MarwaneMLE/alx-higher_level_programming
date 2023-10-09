#!/usr/bin/env python3
def no_c(my_string):
    '''Function that removes all characters c and C from a string'''
    str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            str += ch
    print("{}".format(ch))

