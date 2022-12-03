#!/usr/bin/env python
import argparse
import string
import aocd

from itertools import islice


CHAR_SET = list(string.ascii_lowercase + string.ascii_uppercase)
TEST_DATA_PART_ONE = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")
TEST_DATA_PART_TWO = """vJrwpWtwJgWrhcsFMMfFFhFp
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


def chunk(input_data: list, chunk_size: int = 3) -> list:
    """
    Break a list into chunks of chunk_size elements
    :param input_data:
    :param chunk_size:
    :return:
    """
    input_data = iter(input_data)
    result = iter(lambda : tuple(islice(input_data, chunk_size)), ())
    return result


def split_into_two(line: str) -> list:
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


def intersect(*args) -> str:
    """
    Find the set intersection of multiple strings
    :param string_a:
    :param string_b:
    :return:
    """
    result = "".join(set(args[0]).intersection(*args[1:]))
    return result


def part_one(input_data: list) -> int:
    """
    Find all the common items (characters) in each rucksack (line) when split
    evenly (compartment_a, compartment_b), and calculate the sum of the priorities
    of the common characters
    :return:
    """
    common = ''
    for rucksack in input_data:
        compartment_a, compartment_b = split_into_two(rucksack)
        common += intersect(compartment_a, compartment_b)
    priorities_sum = sum(list(map(lambda x: (CHAR_SET.index(x) + 1), common)))

    return priorities_sum


def part_two(input_data):
    """
    find sum of common item type for each of the 3-line groups of elves in input data
    :param input_data:
    :return:
    """
    common = ''
    for group in chunk(input_data, 3):
        common += intersect(*group)
    priorities_sum = sum(list(map(lambda x: (CHAR_SET.index(x) + 1), common)))
    return priorities_sum

def main() -> None:
    conf = cli()
    if conf.test:
        input_data_part_one = TEST_DATA_PART_ONE
        input_data_part_two = TEST_DATA_PART_TWO
    else:
        input_data_part_one = aocd.lines
        input_data_part_two = aocd.lines

    part_one_result = part_one(input_data_part_one)
    part_two_result = part_two(input_data_part_two)
    print(f"Part One: {part_one_result}")
    print(f"Part Two: {part_two_result}")
    if conf.submit and not conf.test:
        aocd.submit(answer=part_one_result, part=1, day=3, year=2022)
        aocd.submit(answer=part_two_result, part=2, day=3, year=2022)


if __name__ == "__main__":
    main()
