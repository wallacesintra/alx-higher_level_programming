#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiate new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student
        """
        dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return dict
        return self.__dict__
