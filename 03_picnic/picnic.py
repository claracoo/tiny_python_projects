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
        description="What to bring to a Picnic",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food', metavar='food', nargs='+', help='type any word')

    parser.add_argument('-s', '--sorted', action='store_true', help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    food = args.food
    if args.sorted:
        food = sorted(food)
    message = 'You are bringing '

    if len(food) == 0:
        message += 'nothing.'
    elif len(food) == 1:
        message += food[0] + '.'
    elif len(food) == 2:
        message += food[0] + ' and ' + food[1] + '.'
    else:
        for i in range (len(food)):
            if i < len(food) - 1:
                message += food[i] + ', '
            else:
                message += 'and ' + food[-1] + '.'

    print(message)


# --------------------------------------------------
if __name__ == '__main__':
    main()
