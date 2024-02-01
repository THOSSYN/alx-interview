#!/usr/bin/python3
"""Log parsing"""

import sys


def line_parser(line: str):
    """Does line splitting"""
    split_line = line.split()

    ip, _, date, time, query, _, _, status, size = split_line

    return status, int(size)


def print_metric(status_list, total_size):
    """Display metrics for the requests made"""
    print(f"File size: {total_size}")
    for status in sorted(set(status_list)):
        unique_status_count = status_list.count(status)
        print(f"{status}: {unique_status_count}")


def get_metric():
    """Compute metrics read from an API"""
    group_list = []
    total_size = 0
    prev_len = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, size = line_parser(line)

            total_size += size
            group_list.append(status_code)
            list_len = len(group_list)

            if list_len == 10 + prev_len:
                print_metric(group_list, total_size)
                prev_len += 10

    except KeyboardInterrupt:
        print_metric(group_list, total_size)
        raise
    print_metric(group_list, total_size)


# def print_stats(total_size, status_code)
    """Prints the stats of a log file

       Args:
        total_size: is the size of file
        status_code: is the status code returned
    """
    """print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{:s}: {:d}".format(code, count))"""

# def compute_metrics():
    """determines the status code and file_size"""
    """total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = line_parser(line.strip())
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

    print_stats(total_size, status_codes)"""


if __name__ == '__main__':
    get_metric()
