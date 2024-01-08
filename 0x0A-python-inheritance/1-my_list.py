#!/usr/bin/python3
"""print list"""


class MyList(list):
    """list of int elements"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
