#!/usr/bin/python3

class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def running(self):
        print("{} is running".format(self.name))
    def eating(self):
        print("{} is eating".format(self.name))

def main():
    spot = Dog(name="Spot",height=45,weight=40)
    spot.eating()

    fer = Dog()
    fer.name = 'Fer'
    fer.eating()

main()