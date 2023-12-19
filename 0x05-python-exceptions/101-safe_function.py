#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as er:
        print("Exception: {}".format(er))
        result = None
    else:
        return result
