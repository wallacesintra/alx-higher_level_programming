#!/usr/bin/python3
"""
square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of rectangle class"""
    def __init__(self, size):
        """
        instantiate
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
        str representation
        """
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__size, self.__size)
