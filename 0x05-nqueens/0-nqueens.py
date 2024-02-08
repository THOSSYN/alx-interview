#!/usr/bin/python3
"""Nqueen puzzle"""

import sys
from typing import List


def SolveNQueen(n: int) -> List[List[int]]:
    """Determines if n queen can be placed untacked"""
    positive_diagonal = set()
    negative_diagonal = set()
    column = set()
    res = []

    def backtrack(row, placed_queens):
        if row == n:
            res.append(placed_queens[:])
            return

        for col in range(n):
            if col in column or row + col in positive_diagonal or \
                    row - col in negative_diagonal:
                    continue
            positive_diagonal.add(row + col)
            negative_diagonal.add(row - col)
            column.add(col)

            placed_queens.append([row, col])

            backtrack(row + 1, placed_queens)

            positive_diagonal.remove(row + col)
            negative_diagonal.remove(row - col)
            column.remove(col)
            placed_queens.pop()

    backtrack(0, [])
    return res


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = SolveNQueen(n)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
