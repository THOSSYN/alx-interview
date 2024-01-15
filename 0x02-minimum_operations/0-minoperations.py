#!/usr/bin/env python3
"""Determining the number of operatons
   that forms a combination
"""

def minOperations(n: int) -> int:
    """A function that determines the number of operation
       required to form n numbers of H
    """
    if n == 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor += 1

    return operations
