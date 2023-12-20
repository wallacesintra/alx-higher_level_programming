#!/usr/bin/python3
class Quad:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    @property
    def width(self):
        print("getting width")
        return self.__width
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only number for width")
    
    @property
    def length(self):
        print("getting length")
        return self.__length
    
    @length.setter
    def length(self, value):
        if value.isdigit():
            self.__length = value
        else:
            print("Please enter only number for length")   
    
    def areaOfQuad(self):
        return int(self.__width) * int(self.__length)
    
def main():
    square = Quad(width=40,length=40)
    print("Area is {}".format(square.areaOfQuad()))

main()
