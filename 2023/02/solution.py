from functools import reduce
from math import prod
import re

COLORS = {"r": 0, "g": 1, "b": 2}
COLOR_COUNTS = [12, 13, 14]


def parse_data():
    with open("2023/02/input.txt") as f:
        return {
            int(re.search(r"(\d+)", line)[1]): [
                (int(num), color) for num, color in re.findall(r"(\d+) (\w)", line)
            ]
            for line in f
        }


def part_one(data):
    return sum(
        game
        for game, sets in data.items()
        if all(
            c1 <= c2
            for c1, c2 in zip(reduce(reduce_cubes, sets, [0, 0, 0]), COLOR_COUNTS)
        )
    )


def reduce_cubes(cubes, s):
    cubes[COLORS[s[1]]] = max(s[0], cubes[COLORS[s[1]]])
    return cubes


def part_two(data):
    return sum(prod(reduce(reduce_cubes, sets, [0, 0, 0])) for sets in data.values())


def main():
    data = parse_data()

    print(f"Day 02 Part 01: {part_one(data)}")
    print(f"Day 02 Part 02: {part_two(data)}")
