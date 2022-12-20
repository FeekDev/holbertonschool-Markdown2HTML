#!/usr/bin/python3
'''
This file read the comandline
'''

if __name__ == "__main__":
    from sys import argv
    from sys import stderr
    from os import path

    if len(argv) < 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    if not path.exists(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
    else:
        print()
        exit(0)
