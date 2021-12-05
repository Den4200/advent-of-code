import re

import numpy as np


def parse_data():
    with open('2021/05/input.txt') as f:
        data = f.read()

    return [
        ((int(x1), int(y1)), (int(x2), int(y2)))
        for x1, y1, x2, y2 in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", data)
    ]


def draw_line(field, x1, y1, x2, y2):
    if abs(x2 - x1) < abs(y2 - y1):
        field = field.T
        x1, y1, x2, y2 = y1, x1, y2, x2

    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    x = np.arange(x1, x2 + 1)
    y = np.round(((y2 - y1) / (x2 - x1)) * (x - x1) + y1).astype(int)

    field[x, y] += 1


def intersections(data):
    field = np.zeros((1000, 1000), dtype=int)

    for (x1, y1), (x2, y2) in data:
        draw_line(field, x1, y1, x2, y2)

    return (field >= 2).sum()


def part_one(data):
    return intersections(
        ((x1, y1), (x2, y2))
        for (x1, y1), (x2, y2) in data
        if x1 == x2 or y1 == y2
    )


def part_two(data):
    return intersections(data)


def main():
    data = parse_data()

    print(f'Day 05 Part 01: {part_one(data)}')
    print(f'Day 05 Part 02: {part_two(data)}')
