#!/usr/bin/python3
"""Log parsing"""

import sys


def line_parser(line: str):
    """Does line splitting"""
    split_line = line.split()

    ip, _, date, time, query, _, _, status, size = split_line

    return status, size


def get_metric():
    """Compute metrics read from an API"""
    group_list = []
    total_size = 0
    prev_len = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, size = line_parser(line)

            total_size += int(size)

            group_list.append(status_code)

            list_len = len(group_list)

            if list_len == 10 + prev_len:
                print_metric(group_list, total_size)
                prev_len += 10

    except KeyboardInterrupt:
        print_metric(group_list, total_size)
        raise


def print_metric(status_list, total_size):
    """Display metrics for the requests made"""
    print(f"File size: {total_size}")
    for status in sorted(set(status_list)):
        unique_status_count = status_list.count(status)
        print(f"{status}: {unique_status_count}")


if __name__ == '__main__':
    get_metric()
