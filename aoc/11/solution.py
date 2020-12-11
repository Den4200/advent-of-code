from contextlib import suppress

import numpy as np


def parse_data():
    with open('aoc/11/input.txt') as f:
        data = f.read()

    return [list(line) for line in data.splitlines()]


def part_one(data):
    data = np.array(data)
    data[data == 'L'] = '#'

    while True:
        changed = False

        copy = data.copy()
        for (y, x), value in np.ndenumerate(data):
            surroundings = data[
                max(y - 1, 0): min(y + 2, data.shape[0]),
                max(x - 1, 0): min(x + 2, data.shape[1])
            ]

            occupied = len(np.where(surroundings == '#')[0])

            if value == 'L':
                if occupied == 0:
                    copy[y, x] = '#'
                    changed = True

            elif value == '#':
                if occupied >= 5:
                    copy[y, x] = 'L'
                    changed = True

        data = copy

        if not changed:
            return len(np.where(data == '#')[0])


def part_two(data):
    pass


def main():
    data = parse_data()

    print(f'Day 11 Part 01: {part_one(data)}')
    print(f'Day 11 Part 02: {part_two(data)}')
