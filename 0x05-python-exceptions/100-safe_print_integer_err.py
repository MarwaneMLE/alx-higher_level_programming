#!/usr/bin/python3
def safe_print_integer_err(value):
    ''' function that prints an integer.'''
    import sys

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: %s\n" % err)
        return False
