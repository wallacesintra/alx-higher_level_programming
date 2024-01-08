#!/usr/bin/python3
"""
prints square with the character '#'
"""


def print_square(size):
    """ Function to print a square with the character #
    argument:
        size: size of the square printed
    Returns: nothing
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
