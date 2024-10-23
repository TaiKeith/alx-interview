#!/usr/bin/python3
"""
This module contains functions that read stdin line by line and
computes metrics.
"""
import sys
import signal
import re


# Initialize global variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the expected log format
log_pattern = re.compile(
    r'(?P<ip>\S+)\s+-\s+\[(?P<date>.*?)\]\s+"GET /projects/260 HTTP/1.1"\s+'
    r'(?P<status_code>\d+)\s+(?P<file_size>\d+)$'
)


def print_statistics():
    """Print the total file size and status code counts."""
    global total_file_size, status_codes

    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line):
    """Process a single line of input."""
    global total_file_size, status_codes

    match = log_pattern.match(line)
    if match:
        status_code = int(match.group('status_code'))
        file_size = int(match.group('file_size'))

        # Update total file size
        total_file_size += file_size

        # Update the count for the specific status code
        if status_code in status_codes:
            status_codes[status_code] += 1


def signal_handler(sig, frame):
    """Handle CTRL + C (SIGINT) and print the statistics."""
    print_statistics()
    sys.exit(0)


# Set the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read from stdin line by line
    for line in sys.stdin:
        process_line(line)
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle any final statistics print in case of keyboard interruption
    print_statistics()
    sys.exit(0)
