#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_new.append(True)
        else:
            list_new.append(False)
    return list_new
