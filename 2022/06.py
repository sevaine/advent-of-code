#!/usr/bin/env python
import argparse
import aocd

test_data_part_one = [
    {'input': 'bvwbjplbgvbhsrlpgdmjqwftvncz', 'first_marker_pos': 5},
    {'input': 'nppdvjthqldpwncqszvftbrmjlhg', 'first_marker_pos': 6},
    {'input': 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'first_marker_pos': 10},
    {'input': 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 'first_marker_pos': 11}
]

test_data_part_two = [
    {'input': 'mjqjpqmgbljsphdztnvjfqwrcgsmlb', 'first_marker_pos': 19},
    {'input': 'bvwbjplbgvbhsrlpgdmjqwftvncz', 'first_marker_pos': 23},
    {'input': 'nppdvjthqldpwncqszvftbrmjlhg', 'first_marker_pos': 23},
    {'input': 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'first_marker_pos': 29},
    {'input': 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 'first_marker_pos': 26}
]


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


def part_one(in_data):
    """
    for a given input stream the first start of packet marker is when
    4 unique characters in the stream are received.  Return the position of
    the first start of packet marker ( when the last packet of the 4 char marker is received )
    when provided a stream
    :return:
    """
    first_marker_pos = 0
    for i, char in enumerate(in_data):
        start = i
        end = i+4
        slice = in_data[start:end]
        if len(set(slice)) == 4:
            first_marker_pos = end
            break
    return first_marker_pos


def part_two(in_data):
    """
    Now look for messages.  These will be 14 distinct chars instead
    :param in_data:
    :return:
    """
    first_message_marker_pos = 0
    for i, val in enumerate(in_data):
        start = i
        end = i+14
        slice = in_data[start:end]
        if len(set(slice)) == 14:
            first_message_marker_pos = end
            break
    return first_message_marker_pos


def main() -> None:
    conf = cli()
    if conf.test:
        for test_cfg in test_data_part_one:
            result = part_one(test_cfg['input'])
            print(f"part_one -- expected: {test_cfg['first_marker_pos']}, seen: {result}")
            assert result == test_cfg['first_marker_pos']
        for test_cfg in test_data_part_two:
            result = part_two(test_cfg['input'])
            print(f"part_two -- expected: {test_cfg['first_marker_pos']}, seen: {result}")
            assert result == test_cfg['first_marker_pos']
    else:
        result_part_one = part_one(aocd.data.strip())
        result_part_two = part_two(aocd.data.strip())
        print(f"part one: {result_part_one}")
        print(f"part two: {result_part_two}")
        if conf.submit:
            aocd.submit(answer=result_part_one, part=1, day=6, year=2022)
            aocd.submit(answer=result_part_two, part=2, day=6, year=2022)


if __name__ == "__main__":
    main()
