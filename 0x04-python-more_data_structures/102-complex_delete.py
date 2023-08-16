#!/usr/bin/python3
# deletes keys with a specific value in a dictionary

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    if value == a_dictionary.get(value_dic):
        del a_dictionary[value_dic]
        return (a_dictionary)
