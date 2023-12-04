#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_new = ()
    if len(sentence) == 0:
        tuple_new = 0, "None"
    else:
        tuple_new = len(sentence), sentence[0]
    return tuple_new
