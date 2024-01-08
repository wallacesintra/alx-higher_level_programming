#!/usr/bin/python3
"""Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """
    arguments:
        obj: object to check
        a_class: class
    return:
        True(if object is an instance of)
        False(if not)
    """
    if not isinstance(obj, a_class):
        return (False)
    return (True)
