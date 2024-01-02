#!/usr/bin/python3
# Pascal Triangle formation

def pascal_triangle(n):
    """
      A function that returns a list of lists
      of pascal triangle formation

      Args:
        n (int): The levels of pascal triangle desired

      Returns: list of lists
    """
    start_list = [1]  # I initialized a list [1] typical of pascal triangle
    pascal_list = []  # This becomes the list of lists I return

    for _ in range(n):
        pascal_list.append(start_list)  # Loop n, each time append start_list
        new_list = [1]  # each time also list begins with 1
        for i in range(1, len(start_list)):
            """
              starts this loop from index 1. index 0 will always be 1
              in pascal triangle.
              Adds previous index value to current index to get new element
              and then append new element to new_list
            """
            new_listElement = start_list[i - 1] + start_list[i]
            new_list.append(new_listElement)
        new_list.append(1)  # Typically pascal triangle ends with 1
        start_list = new_list
    return pascal_list
