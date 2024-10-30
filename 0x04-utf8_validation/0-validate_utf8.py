#!/usr/bin/python3
"""
This module contains a function that determines if a given data set represents
a valid UTF-8 encoding.
The function returns True if data is a valid UTF-8 encoding, else returns False.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only look at the last 8 bits of each integer (1 byte)
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the character
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1  # 2-byte character
            elif (byte & (mask1 >> 2)) == (mask1 | (mask1 >> 1)):
                num_bytes = 2  # 3-byte character
            elif (byte & (mask1 >> 3)) == (mask1 | (mask1 >> 1) | (mask1 >> 2)):
                num_bytes = 3  # 4-byte character
            else:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if (byte & mask1) != mask1 or (byte & mask2) == mask2:
                return False
            num_bytes -= 1

    return num_bytes == 0
