#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse

def main(args):
    raise NotImplementedError

def parse_args():
    parser = argparse.ArgumentParser(description="Some Description")
    parser.add_argument("some_string", type=str)
    parser.add_argument(
        "some_int",
        type=int,
        help="help goes here",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.some_string, args.some_int)
