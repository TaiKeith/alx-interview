#!/usr/bin/python3
"""
This module contains a function that determines if a given data set represents
a valid UTF-8 encoding.
The function returns True if data is a valid UTF-8 encoding, else
returns False.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    n_bytes, mask1, mask2 = 0, 1 << 7, 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
