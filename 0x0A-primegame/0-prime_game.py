#!/usr/bin/python3
"""A prime game python implementation"""


def isPrime(num):
    """Check if number is prime using dynamic programming"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """Determines the winner of a prime game"""
    for n in nums:
        score_board = {'Maria': 0, 'Ben': 0}
        player_choice = list(range(1, n + 1))
        # Maria's turn
        for i in player_choice:
            if isPrime(i):
                for j in range(i * 2, n + 1, i):
                    if j in player_choice:
                        player_choice.remove(j)
                score_board['Maria'] += 1
                break  # Maria makes one move and then it's Ben's turn
        # Ben's turn
        for j in player_choice:
            if isPrime(j):
                for k in range(j * 2, n + 1, j):
                    if k in player_choice:
                        player_choice.remove(k)
                score_board['Ben'] += 1
    # print("Winner:", max(score_board, key=score_board.get))
    return max(score_board, key=score_board.get)
