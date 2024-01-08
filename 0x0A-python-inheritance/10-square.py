#!/usr/bin/python3
"""Square Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class - subclass of rectangle"""

    def __init__(self, size):
        """instantiate"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
