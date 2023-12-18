try:
    myFile = open("dataTxt.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)

else:
    print("file : ", myFile.read())
    myFile.close()
finally:
    print("Finished working with file.")
