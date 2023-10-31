#!/usr/bin/python3
"""Module for matrix_divided function."""

def matrix_divided(matrix, div):
    """Divide each element in a matrix by a divisor.

    Args:
        matrix (list of lists of ints or floats): 2D list to operate on.
        div (int or float): Divisor for members of the matrix.

    Returns:
        list: A new matrix of quotients for each element of the matrix divided by div.

    Raises:
        TypeError: If the input matrix is not a list of lists of integers/floats.
        TypeError: If the sublists within the matrix are not of the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    """
    new_matrix = []

    # Check if the matrix is a list of lists
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Validate the matrix structure
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide each element and create the new matrix
    for row in matrix:
        new_row = []
        for value in row:
            quotient = round((value / div), 2)
            new_row.append(quotient)
        new_matrix.append(new_row)

    return new_matrix
