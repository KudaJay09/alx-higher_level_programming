#!/usr/bin/python3
<<<<<<< HEAD

class Square:
    def __init__(self, size = 0):
        if not isinstace(size, int):
=======
"""Define a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
>>>>>>> 71884b5a8c7121e44888cd5f389531adfd2591d8
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
