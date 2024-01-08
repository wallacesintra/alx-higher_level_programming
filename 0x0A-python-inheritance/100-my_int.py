#!/usr/bin/python3
"""reverse equality"""


class MyInt(int):
    """subclass of int"""
    def __eq__(self, other_int):
        """reverse =="""
        if self is not other_int:
            return False
        return True

    def __ne__(self, other_int):
        """reverse !="""
        if self is other_int:
            return False
        return True
