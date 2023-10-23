#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''prints x elements of a list.'''
    number = 0

    try:
        for i in range(x):
            print(my_list[i],end="")
            number += 1
    except:
        #Catch an IndexError if there are not enough elements in the list.
        pass
    finally:
        print("")
    return number
