import numpy as np
from scipy.signal import convolve


def parse_data():
    with open('aoc/17/input.txt') as f:
        data = f.read()

    return np.array(
        [[int(value == '#') for value in line] for line in data.splitlines()]
    )


def conway_cubes(data, dimensions):
    kernel = np.ones((3,) * dimensions, dtype=np.int8)
    kernel[(1,) * dimensions] = 0

    cycle = data[(np.newaxis,) * (dimensions - 2) + (...,)]

    for _ in range(6):
        neighbors = convolve(cycle, kernel)
        cycle = (neighbors == 3) | (neighbors == 2) & np.pad(cycle, 1) 

    return cycle.sum()


def part_one(data):
    return conway_cubes(data, 3)


def part_two(data):
    return conway_cubes(data, 4)


def main():
    data = parse_data()

    print(f'Day 17 Part 01: {part_one(data)}')
    print(f'Day 17 Part 02: {part_two(data)}')
