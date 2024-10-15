#!/usr/bin/python3
"""
This module contains a function that takes in a desired number of 'H'
characters and returns the number of operations necessary to achieve exactly n
'H' characters or 0 if it is impossible to achieve
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to get exactly n 'H'
    characters in the text file starting with a single 'H'. The allowed
    operations are 'Copy All' and 'Paste'.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required to achieve exactly n 'H'
            characters, or 0 if it is impossible to achieve.
    """
    # If n is less than 2, it is either impossible or no operations are needed.
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start checking from the smallest possible divisor

    # Factorize the number n
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor  # Reduce n by the divisor factor
        divisor += 1  # Move to the next potential divisor

    return operations
