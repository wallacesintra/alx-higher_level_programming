#!/usr/bin/python3
""" check if it is a sub class """


def inherits_from(obj, a_class):
    """
    function to check if an object is inherited from a specified class
    arguments:
        obj: object
        a_class: class
    return:
        - True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        - False if not
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
