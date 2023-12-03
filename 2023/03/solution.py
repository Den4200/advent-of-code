from collections import defaultdict
from math import prod

import numpy as np


def parse_data():
    with open("2023/03/input.txt") as f:
        return np.pad([[*line.strip()] for line in f], (2, 2), "constant", constant_values=".")


def part_one(data):
    s = 0
    for y, line in enumerate(data[2:-2], start=2):
        x0 = -1

        for x, c in enumerate(line[2:-1], start=2):
            if c.isdigit():
                if x0 == -1:
                    x0 = x

            elif x0 != -1:
                window = data[y - 1:y + 2, x0 - 1:x + 1]

                if np.any((window != ".") & (~np.char.isdigit(window))):
                    s += int("".join(line[x0:x]))

                x0 = -1

    return s


def part_two(data):
    gears = defaultdict(lambda: [])

    for y, line in enumerate(data[2:-2], start=2):
        x0 = -1

        for x, c in enumerate(line[2:-1], start=2):
            if c.isdigit():
                if x0 == -1:
                    x0 = x

            elif x0 != -1:
                window = data[y - 1:y + 2, x0 - 1:x + 1]

                if np.any(window == "*"):
                    dy, dx = np.where(window == "*")
                    gears[y + dy[0] - 1, x0 + dx[0] - 1].append(int("".join(line[x0:x])))

                x0 = -1

    return sum(prod(gear) for gear in gears.values() if len(gear) > 1)


def main():
    data = parse_data()

    print(f"Day 03 Part 01: {part_one(data)}")
    print(f"Day 03 Part 02: {part_two(data)}")
