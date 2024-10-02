#!/usr/bin/python3
"""
This module contains a function that prints the Pascal's Triangle
"""


def pascal_triangle(n):
    """Function that prints out the Pascal's Triangle"""
    triangle = []
    
    for i in range(n):
        # Create a row with 1 at the beginning
        row = [1]
        # If we're beyond the first row, calculate the values between the 1s
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)  # End with 1
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
