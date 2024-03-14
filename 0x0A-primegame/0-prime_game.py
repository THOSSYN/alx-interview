#!/usr/bin/python3
"""A prime game python implementation"""


def isPrime(num):
    """Check if number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(rounds, choice):
    """Determines the winner of a prime game"""
    for n in choice:
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
