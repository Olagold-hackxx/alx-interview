#!/usr/bin/python3
""" Read stdout"""
import sys
import signal
from collections import Counter

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

def print_stdin(st_codes):
    """Print allowed status codes"""
    counter = Counter(st_codes)
    for status, count in counter.items():
        if status in status_codes:
        	print(f"{status}: {count}")


if __name__ == "__main__":
    count = 0
    file_size = 0
    status_codes = []
    try:
        for input in sys.stdin:
            count += 1
            required_input = input.split(" ")
            if count % 10 == 0:
                print ("File size: {}".format(file_size))
                status_codes.sort()
                print_stdin(status_codes)
                status_codes = []
            else:
                if len(required_input) < 9:
                    continue
                else:
                    status_code = int(required_input[7])
                    status_codes.append(status_code)
                    file_size += int(required_input[8])
    except KeyboardInterrupt:
            print ("File size: {}".format(file_size))
            status_codes.sort()
            print_stdin(status_codes)
            sys.exit(0)

