from collections import defaultdict
from functools import partial, reduce
from math import prod

import numpy as np


def parse_data():
    with open("2023/03/input.txt") as f:
        return np.pad([[*line.strip()] for line in f], (2, 2), "constant", constant_values=".")


def gear_windows(data):
    for y, line in enumerate(data[2:-2], start=2):
        x0 = -1

        for x, c in enumerate(line[2:-1], start=2):
            if c.isdigit():
                if x0 == -1:
                    x0 = x

            elif x0 != -1:
                yield x0, x, y, data[y - 1:y + 2, x0 - 1:x + 1]
                x0 = -1


def part_one(data):
    return sum(
        int("".join(data[y][x0:x]))
        for x0, x, y, window in gear_windows(data)
        if np.any((window != ".") & (~np.char.isdigit(window)))
    )


def reduce_gears(data, gears, window_data):
    x0, x, y, window = window_data

    if np.any(window == "*"):
        dy, dx = np.where(window == "*")
        gears[y + dy[0] - 1, x0 + dx[0] - 1].append(int("".join(data[y][x0:x])))

    return gears


def part_two(data):
    return sum(
        prod(gear)
        for gear in reduce(
            partial(reduce_gears, data),
            gear_windows(data),
            defaultdict(lambda: []),
        ).values()
        if len(gear) > 1
    )


def main():
    data = parse_data()

    print(f"Day 03 Part 01: {part_one(data)}")
    print(f"Day 03 Part 02: {part_two(data)}")
