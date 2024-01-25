#!/usr/bin/python3
"""Log Parser"""

import sys


def print_stats(total_size, status_codes):
    """Prints the stats of a log file

       Args:
        total_size: is the size of file
        status_code: is the status code returned
    """
    print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{:s}: {:d}".format(code, count))


def parse_line(line):
    """Parses each each line of stats read

       Args:
        line: is the stats read
    """
    line_parts = line.split()
    if len(line_parts) >= 2:
        return int(line_parts[-1]), line_parts[-2]
    return None, None


def compute_metrics():
    """determines the status code and file_size"""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size, status_code = parse_line(line.strip())
            if file_size is not None and status_code is not None:
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if i % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
