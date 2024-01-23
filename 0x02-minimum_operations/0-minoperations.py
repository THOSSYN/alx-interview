#!/usr/bin/python3
"""An interview preparation project"""


def minOperations(n: int) -> int:
    """A function that determines number of
       copy all and paste operations
    """
    operations = 0
    divisor = 2

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
