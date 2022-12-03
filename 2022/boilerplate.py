#!/usr/bin/env python
import argparse
import aocd


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="advent-of-code cli")
    parser.add_argument(
        "--submit",
        action="store_true",
        required=False,
        default=False,
        help="Submit to Advent Of Code",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        required=False,
        default=False,
        help="Run test functions instead",
    )
    conf = parser.parse_args()
    if conf.test:
        conf.submit = False
    return conf


def part_one():
    pass


def main() -> None:
    conf = cli()
    if conf.submit:
        # Submit parts here
        pass


if __name__ == "__main__":
    main()
