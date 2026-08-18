#!/usr/bin/python3
"""Defines a Pascal's triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle.

    An empty list is returned if n is less than or equal to 0.

    Args:
        n: the number of rows of the triangle.
    """
    triangle = []
    for row in range(n):
        line = [1]
        for i in range(1, row):
            line.append(triangle[row - 1][i - 1] + triangle[row - 1][i])
        if row > 0:
            line.append(1)
        triangle.append(line)
    return triangle
