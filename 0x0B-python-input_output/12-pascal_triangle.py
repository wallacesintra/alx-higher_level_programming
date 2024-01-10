#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function def pascal_triangle(n)
    returns:a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri = tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
