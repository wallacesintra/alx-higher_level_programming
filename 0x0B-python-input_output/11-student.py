#!/usr/bin/python3
"""class Student"""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiate new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        dict = {}
        if isinstance(attrs, list):
            for i in attrs:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
