#!/usr/bin/python3
"""A script for utf-8 validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """A function that validate if an input
       data is utf-8 compliant
    """
    count = 0
    for x in data:
        if count == 0:
            if (x >> 7) == 0b0:
                count = 0
            elif (x >> 5) == 0b110:
                count = 1
            elif (x >> 4) == 0b1110:
                count = 2
            elif (x >> 3) == 0b11110:
                count = 3
            else:
                return False
        else:
            if (x >> 6) != 0b10:
                return False
            count -= 1

    return count == 0
