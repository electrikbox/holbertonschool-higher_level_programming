#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # return [[i ** 2 for i in row] for row in matrix]
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
