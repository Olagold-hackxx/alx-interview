#!/usr/bin/python3
""" Minimum operations"""


def minOperations(n):
    """ Minimum operation """
    if n == 1:
        return 0
    if type(n) != int:
        return 0
    minOp = 0
    value = 1
    copied = 0
    while value < n:
        if n % value != 0:
            minOp = minOp + 1
            value = value + copied
        while n % value == 0 and n > value:
            copied = value
            minOp = minOp + 2
            value = copied + value
    return minOp
