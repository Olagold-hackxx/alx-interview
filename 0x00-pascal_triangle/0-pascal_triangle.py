#!/usr/bin/python3

""" Returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """ Implement pascal"""
    pascal = []
    if n <= 0:
        return pascal
    pascal.append([1])
    for idx in range(1, n):
        row = []
        row.insert(0, 1)
        for col in range(idx - 1):
            row.append(pascal[idx - 1][col] + pascal[idx - 1][col + 1])
        row.append(1)
        pascal.append(row)
    return pascal
