#!/usr/bin/python3
<<<<<<< HEAD
class Square:
    def __init__(self, size = 0):
=======
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
>>>>>>> 71884b5a8c7121e44888cd5f389531adfd2591d8
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
<<<<<<< HEAD
=======

>>>>>>> 71884b5a8c7121e44888cd5f389531adfd2591d8
    def area(self):
        return (self.__size * self.__size)
