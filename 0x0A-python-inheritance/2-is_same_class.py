#!/usr/bin/python3
"""check if its a instance of a class"""


def is_same_class(obj, a_class):
    """
    argument:
        obj: object
        a_class: class
    return:
        True (from the same class),
        False (not from the same class)
    """
    type_a = type(obj)

    if type_a != a_class:
        return False
    return True
