#!/usr/bin/env python
import argparse
import aocd

SHAPES = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}
SCORES = {"rock": 1, "paper": 2, "scissors": 3}
ROUND_SCORING = {"win": 6, "draw": 3, "lose": 0}


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
    return parser.parse_args()


def lookup_by_value(data, choice):
    for k in data:
        if choice in data[k]:
            return k


def play(opponent, me):
    result = None
    if opponent == me:
        result = "draw"
    elif me == "rock" and opponent == "paper":
        result = "lose"
    elif me == "paper" and opponent == "rock":
        result = "win"
    elif me == "rock" and opponent == "scissors":
        result = "win"
    elif me == "scissors" and opponent == "rock":
        result = "lose"
    elif me == "paper" and opponent == "scissors":
        result = "lose"
    elif me == "scissors" and opponent == "paper":
        result = "win"
    return result


def strategy(shape, goal):
    win_conditions = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    lose_conditions = {v: k for k, v in win_conditions.items()}
    me = None
    if goal == "X":
        me = win_conditions.get(shape)
    if goal == "Z":
        me = lose_conditions[shape]
    if goal == "Y":
        me = shape
    return me


def part_one(puzzle_input) -> int:
    scores = []
    for item in puzzle_input:
        opponent, me = [SHAPES[x] for x in item.split()]
        result = play(opponent, me)
        if result == "win":
            scores.append(6 + SCORES[me])
        elif result == "draw":
            scores.append(3 + SCORES[me])
        else:
            scores.append(SCORES[me])
    return sum(scores)


def part_two(puzzle_input) -> int:
    scores = []
    for item in puzzle_input:
        goals = {"X": "lose", "Y": "draw", "Z": "win"}
        opponent, goal = item.split()
        opponent = SHAPES[opponent]
        me = strategy(opponent, goal)
        result = play(opponent, me)
        if result == "win":
            scores.append(6 + SCORES[me])
        elif result == "draw":
            scores.append(3 + SCORES[me])
        else:
            scores.append(SCORES[me])
    return sum(scores)


def test(puzzle_input):
    result_part_one = part_one(puzzle_input)
    result_part_two = part_two(puzzle_input)
    _part_one = result_part_one == 15
    _part_two = result_part_two == 12
    print(f"Test: part_one(): {_part_one}")
    print(f"Test: part_two(): {_part_two}")


def main() -> None:
    conf = cli()
    if conf.test:
        puzzle_input = ["A Y", "B X", "C Z"]
        test(puzzle_input)
    else:
        lines = aocd.lines
        result_part_one = part_one(lines)
        result_part_two = part_two(lines)
        print(f"Part one: {result_part_one}")
        print(f"Part two: {result_part_two}")
        if conf.submit:
            # Submit parts here
            aocd.submit(answer=result_part_one, part=1, day=2, year=2022)
            aocd.submit(answer=result_part_two, part=2, day=2, year=2022)


if __name__ == "__main__":
    main()
