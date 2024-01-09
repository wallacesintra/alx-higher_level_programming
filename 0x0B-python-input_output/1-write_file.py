#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    returns: the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
