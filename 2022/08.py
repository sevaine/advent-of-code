#!/usr/bin/env python
import argparse
import aocd

PART_ONE_TEST_INPUT = """30373
25512
65332
33549
35390""".splitlines()


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


def parse_into_matrix(input_data: list) -> list:
    """
    parse a list of 5 digit numbers into a list of lists of single digit numbers
    :param input_data:
    :return:
    """
    return list(map(lambda x: [int(i) for i in x], input_data))


def is_visible(input_matrix: list, row: int, column: int) -> bool:
    """
    Return True if the outer matrix elements in "cardinal" directions
    are smaller than the one located at intersection of row, column
    :param input_matrix:
    :return:
    """
    tree_height = input_matrix[row][column]
    views = [
        max(input_matrix[row][:column]),
        max(input_matrix[row][column+1:]),
        max([input_matrix[x][column] for x in range(0, row)]),
        max([input_matrix[x][column] for x in range(row+1, len(input_matrix))])
    ]
    seen = False
    for height in views:
        seen = height > tree_height
    return seen


def part_one(in_data):
    matrix = parse_into_matrix(in_data)
    inner_matrix = [x[1:-1] for x in matrix[1:-1]]
    total_trees = sum([len(x) for x in matrix])
    inner_trees = sum([len(x) for x in inner_matrix])
    visible_trees = total_trees - inner_trees
    visible = 0
    for i in range(1, len(matrix) - 1):
        row = matrix[i]
        for j in range(1, len(row) - 1):
            _vis = is_visible(matrix, i, j)
            if _vis:
                visible += 1
    return visible_trees + visible


def main() -> None:
    conf = cli()
    if conf.test:
        print(f"part one: {part_one(PART_ONE_TEST_INPUT)}")
    else:
        res_one = part_one(aocd.lines)
        print(f"part one: {res_one}")
        if conf.submit:
            # Submit parts here
            aocd.submit(part=1, answer=res_one)


if __name__ == "__main__":
    main()
