#!/usr/bin/python3
"""Reading from stdin"""

import fileinput
import sys


if __name__ == '__main__':
    status = []
    unique_status = set()
    file_size = 0

    try:
        for line in fileinput.input():
            line = line.split()
            current_status = int(line[7])
            file_size += int(line[8])
            status.append(current_status)

            if len(status) == 10:
                print(f"File size: {file_size}")
                for unique_item in sorted(set(status)):
                    stat_count = f"{unique_item}: {status.count(unique_item)}"
                    print(stat_count)

                status = []

    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for unique_item in set(status):
            stat_count = f"{unique_item}: {status.count(unique_item)}"
            print(stat_count)
        raise
    sys.exit(0)
