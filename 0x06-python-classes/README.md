OOP - Object Oriented Programming - programming paradigm that uses object to design and organize code.

[class] - template for object, contains attributes and methods that the object will have.

class Dog:
    def __init__(self,name= "",height = 0, weight=0): //initiate an object function
        self.name = name
        self.height = height
        self.weight = weight
    def run(self):
        print("{} is running".format(self.name))
    def eat(self):
        print("{} is eating".format(self.name))
    def bark(self):
        print("{} is barking".format(self.name))

def main():
    spot = Dog("Spot", 66, 26)