#!/usr/bin/python3
<<<<<<< HEAD
class Square:
    def __init__(self, size = 0):
        self.size = size
        
=======
"""Define a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

>>>>>>> 71884b5a8c7121e44888cd5f389531adfd2591d8
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
