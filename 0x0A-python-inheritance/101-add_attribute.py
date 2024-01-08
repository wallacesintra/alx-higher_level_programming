#!/usr/bin/python3
"""add_atribute method"""


def add_attribute(obj, att, val):
    """function to add_atribute method"""
    if hasattr(obj, '__dict__') is True:
        setattr(obj, att, val)
    else:
        raise TypeError("can't add new attribute")
