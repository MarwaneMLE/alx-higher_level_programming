#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Function that returns the weighted average of all integers tuple'''
    if len(my_list) == 0:
        return 0
    else:
        sum_of_mul = 0
        sum_div = 0
        for i in range(len(my_list)):
            sum_of_mul += my_list[i][0] * my_list[i][1]
            sum_div += my_list[i][1]
        return sum_of_mul / sum_div
