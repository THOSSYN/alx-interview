#!/usr/bin/python3
"""Island perimeter problem"""


def island_perimeter(grid):
    """Determines the perimeter of an island
       Island is in form of a row by col grid
    """
    perimeter = 0

    if not grid:
        return perimeter

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
