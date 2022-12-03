#!/usr/bin/env python
import argparse
import string
import aocd

CHAR_SET = list(string.ascii_lowercase + string.ascii_uppercase)
TEST_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
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


def chunk_input(line: str) -> list:
    """
    Break input into 2 halves
    :param line:
    :return:
    """
    chars = list(line)
    split_index = int(len(chars) / 2)
    first_half = "".join(chars[:split_index])
    second_half = "".join(chars[split_index:])
    return [first_half, second_half]


def common_chars(string_a: str, string_b: str) -> str:
    """
    Find the set intersection of string_a and string_b, return as string
    :param string_a:
    :param string_b:
    :return:
    """
    return "".join(set(string_a).intersection(string_b))


def part_one(input_data: list) -> int:
    """
    Find all the common items (characters) in each rucksack (line) when split
    evenly (compartment_a, compartment_b), and calculate the sum of the priorities
    of the common characters
    :return:
    """
    common = ''
    for rucksack in input_data:
        compartment_a, compartment_b = chunk_input(rucksack)
        common += common_chars(compartment_a, compartment_b)
    priorities_sum = sum(list(map(lambda x: (CHAR_SET.index(x) + 1), common)))

    return priorities_sum


def main() -> None:
    conf = cli()
    if conf.test:
        input_data = TEST_DATA
    else:
        input_data = aocd.lines

    part_one_result = part_one(input_data)
    print(f"Part One: {part_one_result}")
    if conf.submit and not conf.test:
        aocd.submit(answer=part_one_result, part=1, day=3, year=2022)


if __name__ == "__main__":
    main()
