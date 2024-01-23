#!/usr/bin/python3
"""Reading from stdin"""

import sys

def process_line(line):
    """Process a line and return (status_code, file_size) if the line is valid."""
    try:
        parts = line.split()
        ip_address, _, _, date, request, status_code, file_size = parts[:7]
        
        if request != '"GET' or not status_code.isdigit() or not file_size.isdigit():
            return None

        return int(status_code), int(file_size)
    except ValueError:
        return None

def print_statistics(file_sizes, status_counts):
    """Print the computed statistics."""
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")

def main():
    """Main function"""
    file_sizes = []
    status_counts = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            result = process_line(line.strip())
            
            if result is not None:
                status_code, size = result
                file_sizes.append(size)
                
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

            if line_number % 10 == 0:
                print_statistics(file_sizes, status_counts)

    except KeyboardInterrupt:
        print_statistics(file_sizes, status_counts)
        sys.exit(1)

if __name__ == "__main__":
    main()
