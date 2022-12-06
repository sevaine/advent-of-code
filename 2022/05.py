#!/usr/bin/env python
import argparse
import aocd
import re

"""
Day 5 - supply stacks.

Part onw appears to be the 'Tower of hanoi' puzzle
"""

TEST_DATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


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


def parse_input(data):
    """
    Parse input data into stack data, and moves
    :param data: Input data in string format
    :return:
    """
    row_re= re.compile("""((?:\\w+)+),?""")
    moves_re = re.compile("""((?:\\d+)+),?""")

    positions_raw = data.split("\n\n")[0].split("\n")[:-1]
    moves_raw = data.split("\n\n")[1].strip().split("\n")
    stacks_raw = data.split("\n\n")[0].split("\n")[-1]
    stack_names = row_re.findall(stacks_raw)
    positions = [[] for x in range(len(row_re.findall(stacks_raw)))]

    for row in positions_raw:
        for i in stack_names:
            stack_item = row[stacks_raw.find(i)]
            if stack_item != ' ':
                positions[int(i)-1].append(stack_item)
            else:
                continue

    moves = [moves_re.findall(i) for i in moves_raw]

    return positions, stack_names, moves


def part_one(in_data):
    positions, stack_names, moves = parse_input(in_data)
    for move in moves:
        n, src, dst = [int(i) for i in move]
        for box in range(n):
            value = positions[src-1].pop(0)
            positions[dst-1].insert(0, value)
    top_boxes = []
    for stack in positions:
        top_boxes.append(stack[0])
    return ''.join(top_boxes)


def part_two(in_data):
    positions, stack_names, moves = parse_input(in_data)
    for move in moves:
        n, src, dst = [int(i) for i in move]
        slice = positions[src-1][:n]
        del positions[src-1][0:n]
        if not positions[src-1]:
            positions[src-1] = []
        positions[dst-1] = slice + positions[dst-1]

    top_boxes = []
    for stack in positions:
        top_boxes.append(stack[0])
    return ''.join(top_boxes)


def main() -> None:
    conf = cli()
    if conf.test:
        result_1 = part_one(TEST_DATA)
        result_2 = part_two(TEST_DATA)
        print(result_1)
        print(result_2)
    else:
        result_1 = part_one(aocd.data)
        result_2 = part_two(aocd.data)
        print(result_1)
        print(result_2)
        if conf.submit:
            aocd.submit(result_1, part=1, day=5, year=2022)
            aocd.submit(result_2, part=2, day=5, year=2022)


if __name__ == "__main__":
    main()
