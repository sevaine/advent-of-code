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


def part_one(input_data):
    """
    work out which elf assignments are fully contained by other elves' assignments
    return the number of assignment pairs where one fully contains the other
    :return:
    """
    fully_contained_count = 0
    for elf in input_data:
        fields = [set(range([int(i) for i in j.split("-")][0], [int(i) for i in j.split("-")][-1] + 1)) for j in elf.split(",")]
        if fields[0].issubset(fields[1]) or fields[1].issubset(fields[0]):
            fully_contained_count += 1
    return fully_contained_count


def test_part_one():
    print(f"Part One: {part_one(TEST_INPUT_PART_ONE)}")


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
