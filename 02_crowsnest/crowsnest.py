#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='type any word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    word = args.word
    specifier = ''
    if word[0].lower() in 'aeiou':
        specifier = 'an'
    else:
        specifier = 'a'

    print('Ahoy, Captain, ' + specifier + ' ' + word + ' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
