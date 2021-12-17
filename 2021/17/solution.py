import re
from itertools import product
from math import sqrt


def parse_data():
    with open('2021/17/input.txt') as f:
        data = f.read()

    return [int(num) for num in re.findall(r"(-?\d+)", data)]


def find_max_height(xmin, xmax, ymin, ymax, dx, dy):
    x = 0
    y = 0
    max_height = None

    while x < xmax and y > ymin:
        x += dx
        y += dy

        dx -= dx // abs(dx) if dx > 0 or dx < 0 else 0
        dy -= 1

        if max_height is None or y > max_height:
            max_height = y

        if xmin <= x <= xmax and ymin <= y <= ymax:
            return max_height


def part_one(data):
    ymin = data[2]
    return ymin * (ymin + 1) // 2


def part_two(data):
    xmin, xmax, ymin, _ = data

    return sum(
        find_max_height(*data, dx, dy) is not None
        for dx, dy in product(
            range(int(sqrt(2 * xmin)), xmax + 1),
            range(ymin, abs(ymin)),
        )
    )


def main():
    data = parse_data()

    print(f'Day 17 Part 01: {part_one(data)}')
    print(f'Day 17 Part 02: {part_two(data)}')
