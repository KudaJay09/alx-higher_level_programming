#!/usr/bin/python3
# adds all unique integers in a list

def uniq_add(my_list=[]):
    number = 0

    for element in set(my_list):
        number += element

        return number
