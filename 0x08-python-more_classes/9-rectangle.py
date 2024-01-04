#!/usr/bin/python3


"""
rectangle class
"""


class Rectangle():
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """private attributes width and height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (int(self.__height) + int(self.__width)) * 2

    def __str__(self) -> str:
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""

        area = ""
        for i in range(self.__height):
            for x in range(self.__width):
                print(self.print_symbol, end="")
            if i < self.__height - 1:
                print()
        return (area)

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """eturns a new Rectangle instance
        with width == height == size"""
        return cls(size, size)
