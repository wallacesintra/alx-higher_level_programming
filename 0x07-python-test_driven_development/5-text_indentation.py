#!/usr/bin/python3
"""
print 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function to print 2 new lines after ".?:" characters
    arguments:
        text:string
    Returns: Nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    st = text[:]

    for d in ".?:":
        list_text = st.split(d)
        st = ""
        for i in list_text:
            i = i.strip(" ")
            st = i + d if st is "" else st + "\n\n" + i + d

    print(st[:-3], end="")
