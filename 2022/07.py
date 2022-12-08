#!/usr/bin/env python
import argparse
import aocd
import fs
import re


TEST_DATA = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()


def make_fs(in_data):
    """
    parse data into an in memory filesystem. Store file sizes inside file names for convenience
    :param in_data:
    :return:
    """
    mem_fs = fs.open_fs("mem://")
    path = []
    for line in in_data:
        fields = line.split()
        if fields[1] == "ls":
            continue
        if fields[1] == "cd":
            cdarg = fields[-1]
            if cdarg == "..":
                path = path[:-1]
            elif cdarg == "/":
                path.append("")
            else:
                path.append(cdarg)
            if not mem_fs.exists("/".join(path)):
                mem_fs.makedir("/".join(path))
            continue
        if fields[0].isnumeric():
            file_name = "/".join(path + [fields[-1]])
            with mem_fs.open(file_name, "wb") as fh:
                fh.seek(int(fields[0]) - 1)
                fh.write(b"\0")
            continue
    return mem_fs


def dir_size(filesystem, dirname, size=0):
    """
    Recursive dirsize sum function
    :param filesystem:
    :param dir:
    :return:
    """
    # import pdb; pdb.set_trace()
    for i in filesystem.walk(dirname):
        for subdir in i.dirs:
            subdir.name
            if filesystem.exists(f"{dirname}/{subdir}"):
                size += dir_size(filesystem, subdir.name, size)
        for file in i.files:
            size += filesystem.getinfo(
                f"{i.path}/{file.name}", namespaces=["details"]
            ).size
    return size


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
    Solve this using an in-memory filesystem, because at heart I'm still a sysadmin :P
    :param in_data:
    :return:
    """
    filesystem = make_fs(in_data)
    paths = {d.path: 0 for d in filesystem.walk("/")}
    for path in paths:
        total_size = dir_size(filesystem, path)
        paths[path] = total_size
    return sum([size for size in paths.values() if size <= 100000]), paths


def part_two(paths):
    """
    take actions to free up space by removing the smallest of dirs to provide 30000000 free space
    """
    fs_size = 70000000
    free_space = fs_size - paths["/"]
    candidates = {}
    for d, s in paths.items():
        new_free_space = free_space + s
        if new_free_space > 30000000:
            candidates[d] = s
    print(candidates)

    return min(candidates.values())


def main() -> None:
    conf = cli()
    if conf.test:
        result_1, path_sizes = part_one(TEST_DATA)
        result_2 = part_two(path_sizes)
        print(f"part one: {result_1}")
        print(f"part two: {result_2}")
        assert result_1 == 95437
    else:
        result_1, path_sizes = part_one(aocd.lines)
        result_2 = part_two(path_sizes)
        print(f"part one: {result_1}")
        print(f"part two: {result_2}")
        if conf.submit:
            # Submit parts here
            aocd.submit(part=1, answer=result_1)
            aocd.submit(part=2, answer=result_2)


if __name__ == "__main__":
    main()
