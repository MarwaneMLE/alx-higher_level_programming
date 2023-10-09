#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ''' function that adds 2 tuples'''
    new_tuple = ()
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
