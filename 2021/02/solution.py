import re

import numpy as np


def parse_data():
    with open('2021/02/input.txt') as f:
        data = f.read()

    return [(d, int(amt)) for d, amt in re.findall(r"(\w+) (\d+)", data)]


def part_one(data):
    directions = {
        "forward": np.array([1, 0]),
        "up": np.array([0, -1]),
        "down": np.array([0, 1]),
    }

    return np.array([directions[d] * amt for d, amt in data]).sum(axis=0).prod()


def part_two(data):
    x = 0
    depth = 0
    aim = 0

    for direction, amount in data:
        if direction == "forward":
            x += amount
            depth += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    return depth * x


def main():
    data = parse_data()

    print(f'Day 02 Part 01: {part_one(data)}')
    print(f'Day 02 Part 02: {part_two(data)}')
