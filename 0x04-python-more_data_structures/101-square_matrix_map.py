#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
        function that computes the square
        value of all integers of a matrix using map
    """
    return list(map(lambda i: list(map(lambda x: x**2, i)), matrix))
