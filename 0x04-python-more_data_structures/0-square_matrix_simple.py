#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def list_square(array):
        new_matrix = []
        for num in array:
            new_matrix.append(num ** 2)
    return new_matrix

