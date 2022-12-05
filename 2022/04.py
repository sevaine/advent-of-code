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


def ranges_overlap(range_declaration: str) -> bool:
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
    return sum([1 for i in input_data if ranges_overlap(i)])


def test_part_one():
    print(f"Part One: {part_one(TEST_INPUT_PART_ONE)}")


def part_two(input_data):
    """
    Same as part one, but now we want to know where a section fully contains any other section, not just
    for a single elf
    :return:
    """



def main() -> None:
    conf = cli()
    if conf.test:
        test_part_one()
    else:
        part_one_answer = part_one(aocd.lines)
        print(f"Part One: {part_one_answer}")

        if conf.submit:
            aocd.submit(part_one_answer, day=4, year=2022, part=1)


if __name__ == "__main__":
    main()
