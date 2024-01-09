#!/usr/bin/python3
import os

with open("data.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some text\nMore text\nEven more text")

with open("data.txt", encoding="utf-8") as myFile:
    print(myFile.read()) ##read entire file


print(myFile.closed)##checks if the file is closed(True / False)
print(myFile.name)##returns file's name
print(myFile.mode) ##return the last mode used


"""
rename file
-----------
os.rename("currentfileName", "newFileName")
os.rename("data.txt", "newData.txt")


remove file
-----------
os.remove("fileName")

make directory
--------------
os.mkdir("dirName")


remove directory
-----------------
os.rmdir("dirName")


change directory
----------------
os.chdir("dirToName")


show current directory
----------------------
print(os.getcwd())
"""

