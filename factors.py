#!/usr/bin/python3

import sys
from math import isqrt

def factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return f"{n}={i}*{n//i}"
    return f"{n}=1*{n}"

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                num = int(line.strip())
                print(factorize(num))
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except ValueError:
        print(f"Invalid number in the file: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
