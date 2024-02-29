#!/usr/bin/python3
"""Minimum coins for making change"""


def makeChange(coins, total):
    """Minimum coin algorithm"""
    if total <= 0:
        return 0

    # Initialize the DP array with a size of total + 1
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Calculate minimum coins needed for each value from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            # Check if the current coin denomination can be used
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, total cannot be met
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
