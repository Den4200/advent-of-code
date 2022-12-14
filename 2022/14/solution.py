from copy import deepcopy
import re

import numpy as np


def parse_data():
    with open("2022/14/input.txt") as f:
        data = f.read()

    grid = np.zeros((1000, 1000))
    paths = [
        [
            tuple(int(coord) for coord in re.findall(r"(\d+)", coords))
            for coords in line.split(" -> ")
        ]
        for line in data.splitlines()
    ]

    max_y = 0
    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1

                x = x1
                y = np.arange(y1, y2 + 1)

                max_y = max(y2, max_y)
            else:
                if x1 > x2:
                    x1, x2 = x2, x1

                x = np.arange(x1, x2 + 1)
                y = y1

                max_y = max(y1, max_y)

            grid[y, x] = 1

    return grid, max_y


def part_one(data):
    grid, max_y = deepcopy(data)
    sand = 0

    while True:
        sand_pos = (0, 500)
        grid[sand_pos] = 2

        while True:
            if sand_pos[0] > max_y:
                return sand

            if grid[(new_y := sand_pos[0] + 1), sand_pos[1]] == 0:
                grid[sand_pos] = 0
                sand_pos = (new_y, sand_pos[1])
                grid[sand_pos] = 2
                continue
            elif (
                grid[(new_y := sand_pos[0] + 1), (new_x := sand_pos[1] - 1)] == 0
                or grid[(new_y := sand_pos[0] + 1), (new_x := sand_pos[1] + 1)] == 0
            ):
                grid[sand_pos] = 0
                sand_pos = (new_y, new_x)
                grid[sand_pos] = 2
                continue

            break

        sand += 1


def part_two(data):
    grid, max_y = data
    grid[max_y + 2, np.arange(1000)] = 1

    sand = 0
    while True:
        sand_pos = (0, 500)
        grid[sand_pos] = 2

        while True:
            if grid[(new_y := sand_pos[0] + 1), sand_pos[1]] == 0:
                grid[sand_pos] = 0
                sand_pos = (new_y, sand_pos[1])
                grid[sand_pos] = 2
                continue
            elif (
                grid[(new_y := sand_pos[0] + 1), (new_x := sand_pos[1] - 1)] == 0
                or grid[(new_y := sand_pos[0] + 1), (new_x := sand_pos[1] + 1)] == 0
            ):
                grid[sand_pos] = 0
                sand_pos = (new_y, new_x)
                grid[sand_pos] = 2
                continue

            break

        sand += 1

        if sand_pos == (0, 500):
            return sand


def main():
    data = parse_data()

    print(f"Day 14 Part 01: {part_one(data)}")
    print(f"Day 14 Part 02: {part_two(data)}")
