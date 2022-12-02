#!/usr/bin/env python

import aocd


def main():
    data = aocd.get_data(day=1, year=2022)

    elves = []
    elf = 0
    tmp_index = 0
    # get the elf and calories into a list of tuples
    for idx in [x for x in range(len(aocd.lines)) if aocd.lines[x] == ""]:
        elves.append((elf, (sum([int(i) for i in aocd.lines[tmp_index:idx]]))))
        tmp_index = idx + 1
        elf += 1

    # sort elves tuples by calories
    sorted_elves = sorted(elves, key=lambda x: x[1], reverse=True)

    # Part 1
    max_calories = sorted_elves[0][1]

    # Part 2
    group_calories = sum([x[1] for x in sorted_elves[0:3]])

    # submit
    # aocd.submit(answer=max_calories, part=1, day=1, year=2022)
    # aocd.submit(answer=group_calories, part=2, day=1, year=2022)

    print("Done.")


if __name__ == "__main__":
    main()
