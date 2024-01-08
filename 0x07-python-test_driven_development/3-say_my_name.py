#!/usr/bin/python3
"""
prints text
"""


def say_my_name(first_name, last_name=""):
    """ Function to print "My name is <first name> <last name>"
    arguments:
        first_name: firstname
        last_name: lastname

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
