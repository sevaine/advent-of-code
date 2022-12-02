#!/usr/bin/env python
import argparse
import aocd


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="advent-of-code cli")
    parser.add_argument('--submit', action='store_true', required=False, default=False, help="Submit to Advent Of Code")
    return parser.parse_args()


def part_one():
    pass


def main() -> None:
    conf = cli()
    if conf.submit:
        # Submit parts here

if __name__ == '__main__':
    main()