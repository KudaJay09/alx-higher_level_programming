#!/usr/bin/python3

"""Define a funnction that searches for object attribute"""


def lookup(obj):
    """Return a list of an object attributes available"""
    return (dir(obj))
