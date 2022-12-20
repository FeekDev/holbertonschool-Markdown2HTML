#!/usr/bin/python3
'''
This file read the comandline
'''

from sys import argv
from sys import stderr
from os import path

if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    elif not path.exists(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
    else:
        exit(0)
