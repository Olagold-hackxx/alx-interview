#!/usr/bin/python3
""" Read stdout"""
import sys

def print_stats(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def process_line(line, total_size, status_codes):
    parts = line.split()
    if len(parts) != 7:
        return total_size, status_codes

    ip, _, _, status_code, size = parts
    if not status_code.isdigit():
        return total_size, status_codes

    status_code = int(status_code)
    if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
        return total_size, status_codes

    total_size += int(size)
    status_codes[status_code] = status_codes.get(status_code, 0) + 1
    return total_size, status_codes

def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = process_line(line.strip(), total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
                print()

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
