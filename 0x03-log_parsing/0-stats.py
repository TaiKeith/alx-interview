#!/usr/bin/python3
"""
This module contains functions that read stdin line by line and
computes metrics.
"""
import sys
import re


def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    log_fmt = (
            r'(?P<ip>\S+) - \[(?P<date>.*?)\] '
            r'"(?P<request>[^"]*)" (?P<status_code>\d{3}) '
            r'(?P<file_size>\d+)'
            )

    info = {
        'status_code': '0',
        'file_size': 0,
    }

    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        info['status_code'] = resp_match.group('status_code')
        info['file_size'] = int(resp_match.group('file_size'))

    return info


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print(f'{status_code}: {num}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """
    Starts the log parser.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }

    try:
        # Read from stdin line by line
        for line in sys.stdin:
            total_file_size = update_metrics(
                line.strip(),
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Print final statistics in case of interruption
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
