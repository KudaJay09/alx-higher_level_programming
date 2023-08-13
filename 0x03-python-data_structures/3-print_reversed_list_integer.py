#!/usr/bin/python3
# integers of a list, in reverse order.

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in my_list:
            print("{:d}".format(i))
