#!/usr/bin/python3
"""
This module contains a function `def island_perimeter(grid)` that returns
the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island, grid
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                perimeter += 4
                if row > 0:
                    perimeter = perimeter - grid[row - 1][col]
                if row < len(grid) - 1:
                    perimeter = perimeter - grid[row + 1][col]
                if col > 0:
                    perimeter = perimeter - grid[row][col - 1]
                if col < len(grid) - 1:
                    perimeter = perimeter - grid[row][col + 1]
    return perimeter
