#unsafe python program to demonstrate CodeQL 

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: program.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if os.path.exists(filename):
        with open(filename) as f:
            print(f.read())
    else:
        print("Error: {} not found".format(filename))
        sys.exit(1)
        