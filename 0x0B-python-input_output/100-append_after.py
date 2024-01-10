#!/usr/bin/python3
"""Log parsing"""


def append_after(filename="", search_string="", new_string=""):
    """
    script that reads stdin line by line and computes metrics
    """
    txt = ""
    with open(filename) as myFile:
        for line in myFile:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as file:
        file.write(txt)
