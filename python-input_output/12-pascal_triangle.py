#!/usr/bin/python3
"""print Pascal triangle"""


def pascal_triangle(n):
    """print Pascal triangle
    Args:
        n (triangle height): number of row
    Returns:
        list: triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        previous_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(previous_row)):
            new_value = previous_row[i - 1] + previous_row[i]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
