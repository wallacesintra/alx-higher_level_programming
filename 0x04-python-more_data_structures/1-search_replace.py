#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    my_list : the initial list
    search : the element to replace in the list
    replace : the new element
    '''
    new = my_list.copy()
    i = new.index(search)
    new.insert(i, replace)
    return new
