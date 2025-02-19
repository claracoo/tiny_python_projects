#!/usr/bin/env python3
"""Howler"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', type=str, help='Input string or file')

    parser.add_argument('-o', '--outfile', help='Output filename', metavar='str', type=str, default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outfile = open(args.outfile, 'w') if args.outfile else sys.stdout
    outfile.write(args.text.upper() + '\n')
    outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
