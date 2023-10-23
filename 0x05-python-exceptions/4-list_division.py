#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ''' function that divides element by element 2 lists.'''
    # Initialize an empty list to store the division results.
    result_list = []

    try:
        for i in range(list_length):
            try:
                # Perform the element-wise div  and append the result to list
                result = my_list_1[i] / my_list_2[i]
                result_list.append(result)
            except ZeroDivisionError:
                # Catch a ZeroDivisionError if division by zero occurs.
                result_list.append(0)
            except (TypeError, ValueError):
                #Catch TypeError or ValueError if the elements can't be divided
                print("wrong type")
                result_list.append(0)
            except IndexError:
                # Catch IndexError if my_list_1 or my_list_2 is too short.
                print("out of range")
                result_list.append(0)
    finally:
        # Ensure the result_list has the desired length
        while len(result_list) < list_length:
            result_list.append(0)

    return result_list

