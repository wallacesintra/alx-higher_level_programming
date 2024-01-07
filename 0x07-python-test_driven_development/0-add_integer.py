#!/usr/bin/python3
"""adds 2 integers"""


def add_integer(a, b=98):
    """ function to add two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    """

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("a must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)