#!/usr/bin/python3
"""
This module contains a function that given a pile of coins of different values,
determines the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet the given amount.

    Args:
        coins (List): List of values of the coins in your possession.
        total (int): The total amount which you need to make change.

    Returns:
        (int) - The fewest number of coins needed to meet total
    """
    if total < 1:
        return 0

    # Initialize the dynamic programming table.
    change = [float('inf')] * (total + 1)
    change[0] = 0

    # Fill the dynamic programming table
    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                change[i] = min(change[i], change[i - coins[j]] + 1)

    # return the result
    return change[total] if change[total] != float('inf') else -1
