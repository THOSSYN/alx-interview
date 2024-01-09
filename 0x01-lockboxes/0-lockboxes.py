#!/usr/bin/python3
"""Determine if all boxes could be unlocked"""


def canUnlockAll(boxes):
    """A function that checks if all boxes can be opened"""
    size = len(boxes)
    keys = [0]

    for key in keys:
        for boxkey in boxes[key]:
            if boxkey not in keys and boxkey < size:
                keys.append(boxkey)

    return len(keys) == size
