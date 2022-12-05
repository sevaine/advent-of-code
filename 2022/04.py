#!/usr/bin/env python
import argparse
import aocd


TEST_INPUT_PART_ONE = [x.strip() for x in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()]


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


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + list_of_lists[1:]


def get_ranges(items: list) -> list:
    """
    turn input data in to a list of range()
    :param items: The input data
    :return:
    """
    for line in items:
        fields = line.split(",")
        yield [string_to_range(fields[0]), string_to_range(fields[1])]


def string_to_range(in_data):
    conversion = list(map(lambda x: int(x), in_data.split("-")))
    return range(conversion[0], conversion[-1] + 1)


def is_fully_contained(range_declaration: str) -> bool:
    """
    return True if range_a is fully contained by range_b, or vice versa
    :param range_declaration: the ranges declaration in format "N-N,N-N"
    :return:
    """
    fields = [set(range([int(i) for i in j.split("-")][0], [int(i) for i in j.split("-")][-1] + 1)) for j in range_declaration.split(",")]
    if fields[0].issubset(fields[1]) or fields[1].issubset(fields[0]):
        return True
    return False


def part_one(input_data):
    """
    work out which elf assignments are fully contained by other elves' assignments
    return the number of assignment pairs where one fully contains the other
    :return:
    """
    return sum([1 for i in input_data if is_fully_contained(i)])


def test_part_one():
    print(f"Part One: {part_one(TEST_INPUT_PART_ONE)}")


def part_two(input_data):
    """
    Same as part one, but now we want to know where a section fully contains any other section, not just
    for a single elf
    :return:
    """
    ranges = list(get_ranges(input_data))
    ranges_overlapping = 0
    while ranges:
        to_check = ranges.pop()
        if set(to_check[0]).intersection(to_check[1]):
            ranges_overlapping += 1
    return  ranges_overlapping


def test_part_two():
    print(f"Part Two: {part_two(TEST_INPUT_PART_ONE)}")


def main() -> None:
    conf = cli()
    if conf.test:
        test_part_one()
        test_part_two()
    else:
        part_one_answer = part_one(aocd.lines)
        print(f"Part One: {part_one_answer}")

        part_two_answer = part_two(aocd.lines)
        print(f"Part Two: {part_two_answer}")

        if conf.submit:
            aocd.submit(part_one_answer, day=4, year=2022, part=1)
            aocd.submit(part_two_answer, day=4, year=2022, part=2)


if __name__ == "__main__":
    main()
