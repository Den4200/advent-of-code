import itertools

import numpy as np


def parse_data():
    with open('aoc/11/input.txt') as f:
        data = f.read()

    return np.array([list(line) for line in data.splitlines()])


def part_one(data):
    data[data == 'L'] = '#'

    height, width = data.shape

    while True:
        changed = False

        buffer = data.copy()
        for (y, x), value in np.ndenumerate(data):
            surroundings = buffer[
                max(y - 1, 0): min(y + 2, height),
                max(x - 1, 0): min(x + 2, width)
            ]

            occupied = len(np.where(surroundings == '#')[0])

            if value == 'L':
                if occupied == 0:
                    data[y, x] = '#'
                    changed = True

            elif value == '#':
                if occupied >= 5:
                    data[y, x] = 'L'
                    changed = True

        if not changed:
            return len(np.where(data == '#')[0])


def part_two(data):
    data[data == 'L'] = '#'

    height, width = data.shape

    while True:
        changed = False

        buffer = data.copy()
        for (y, x), value in np.ndenumerate(data):
            occupied = 0

            for dy, dx in itertools.product((-1, 0, 1), repeat=2):
                if dy == dx == 0:
                    continue

                for i in itertools.count(1):
                    sy = y + i * dy
                    sx = x + i * dx

                    if not 0 <= sy < height or not 0 <= sx < width:
                        break

                    if (seat := buffer[sy, sx]) != '.':
                        if seat == '#':
                            occupied += 1
                        break

            if value == 'L':
                if occupied == 0:
                    data[y, x] = '#'
                    changed = True

            elif value == '#':
                if occupied >= 5:
                    data[y, x] = 'L'
                    changed = True

        if not changed:
            return len(np.where(data == '#')[0])


def main():
    data = parse_data()

    print(f'Day 11 Part 01: {part_one(data)}')
    print(f'Day 11 Part 02: {part_two(data)}')
