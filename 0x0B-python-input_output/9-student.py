#!/usr/bin/python3
"""class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiate
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of Student Class"""
        return self.__dict__
