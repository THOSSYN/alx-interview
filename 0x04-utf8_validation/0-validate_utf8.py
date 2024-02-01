#!/usr/bin/python3
"""A script for utf-8 validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """A function that validate if an input
       data is utf-8 compliant
    """
    count = 0

    for item in data:
        if count == 0:
            if (item >> 5) == '0b110':
                count = 1
            elif (item >> 4) == '0b1110':
                count = 2
            elif (item >> 3) == '0b11110':
                count = 3
            elif (item >> 7) != 0:
                return False
        else:
            if (item >> 6) != '0b10':
                return False
            count -= 1
    return count == 0
