#!/usr/bin/python3

"""Define an inherited list classMy List"""


class MyList(list):
    """Sorted printing dor the built-in list class"""

    def print_sorted(self):
        """Print list in sorted ascending order"""
        print(sorted(self))
