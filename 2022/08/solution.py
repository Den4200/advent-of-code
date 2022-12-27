from itertools import product

import numpy as np


def parse_data():
    with open("2022/08/input.txt") as f:
        data = f.read()

    return np.array([[int(h) for h in line] for line in data.splitlines()])


def get_visible_path(height_map, reverse=False):
    positions = set()

    for y, row in enumerate(height_map[1:-1], start=1):
        highest = row[0]

        for x, val in enumerate(row[1:], start=1):
            if val > highest:
                if reverse:
                    positions.add((y, x))
                else:
                    positions.add((x, y))

                highest = val

    for y, row in enumerate(height_map[1:-1], start=1):
        highest = row[-1]

        for x, val in enumerate(reversed(row[:-1]), start=1):
            if val > highest:
                if reverse:
                    positions.add((y, len(row) - x - 1))
                else:
                    positions.add((len(row) - x - 1, y))

                highest = val

    return positions


def part_one(data):
    flat_indices = product(range(len(data)), range(len(data[0])))
    indices = np.array([*flat_indices]).reshape((len(data), len(data[0]), 2))

    positions = {
        *map(tuple, indices[0,]),
        *map(tuple, indices[-1,]),
        *map(tuple, indices[:,0]),
        *map(tuple, indices[:,-1]),
    }

    positions |= get_visible_path(data)
    positions |= get_visible_path(data.T, reverse=True)

    return len(positions)


def part_two(data):
    highest = 0

    for y, row in enumerate(data[1:-1], start=1):
        for x, val in enumerate(row[1:-1], start=1):
            scenic_score = 1

            score = 0
            for v in row[x + 1:]:
                score += 1

                if v >= val:
                    break

            scenic_score *= score

            score = 0
            for v in reversed(row[:x]):
                score += 1

                if v >= val:
                    break

            scenic_score *= score

            score = 0
            for v in data[y + 1:]:
                score += 1

                if v[x] >= val:
                    break

            scenic_score *= score

            score = 0
            for v in reversed(data[:y]):
                score += 1

                if v[x] >= val:
                    break

            scenic_score *= score

            if scenic_score > highest:
                highest = scenic_score

    return highest


def main():
    data = parse_data()

    print(f"Day 08 Part 01: {part_one(data)}")
    print(f"Day 08 Part 02: {part_two(data)}")
