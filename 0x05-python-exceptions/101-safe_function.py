#!/usr/bin/python3

def safe_function(fct, *args):
    '''function that executes a function safely.'''
    import sys

    try:
        res = fct(*args)
    except BaseException as e:
        res = None
        sys.stderr.write("Exception: %s\n" % e)
    return res
