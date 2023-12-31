#!/usr/bin/python3
"""
Rectangle Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class is a subclass of BaseGeometry"""

    def __init__(self, width, height):
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width
