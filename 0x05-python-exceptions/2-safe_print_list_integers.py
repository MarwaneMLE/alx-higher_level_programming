#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''  prints the first x elements of a list and only integers '''
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            # check if the value is an integer
            if isinstance(value, int):
                print("{:d}".format(value, end=" "))
                count += 1
    except (IndexError, ValueError):
        pass

    print("")

    return count
