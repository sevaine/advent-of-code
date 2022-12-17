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


def parser(input_data: list) -> list:
    """
    parse input, and return a list
    :param input_data:
    :return:
    """
    trees = list(map(lambda x: [int(i) for i in x], input_data))
    visible = list(map(lambda x: [False for i in x], input_data))
    return trees, visible


def get_column(trees, column):
    return [trees[x][column] for x in range(len(trees))]


def find_visible_trees(trees, visible):
    """
    Return True if the outer matrix elements in "cardinal" directions
    are smaller than the one located at intersection of row, column
    :param input_matrix:
    :return:
    """
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            tree_height = trees[row][col]
            if row == 0 or row == len(trees) - 1:
                visible[row][col] = True
            elif col == 0 or col == len(trees[row]) - 1:
                visible[row][col] = True
            else:
                from_left = max(trees[row][:col])
                from_right = max(trees[row][col + 1:])
                from_top = max(get_column(trees, col)[:row])
                from_bottom = max(get_column(trees, col)[row + 1:])
                visible[row][col] = (tree_height > from_left or tree_height > from_right or tree_height > from_top or tree_height > from_bottom)
    return visible


def part_one(in_data):
    trees, visible = parser(in_data)
    visible = find_visible_trees(trees, visible)
    return len([b for a in visible for b in a if b is True])


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
