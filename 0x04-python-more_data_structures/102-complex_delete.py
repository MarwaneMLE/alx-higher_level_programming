#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary.'''
    list_keys = list(a_dictionary.keys())

    for val_dic in list_keys:
        if value == a_dictionary.get(val_dic):
            del a_dictionary[val_dic]
        return a_dictionary
