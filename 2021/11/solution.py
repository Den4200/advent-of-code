import itertools
import re

import numpy as np
from scipy.ndimage import convolve

KERNEL = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]


def parse_data():
    with open('2021/11/input.txt') as f:
        data = f.read()

    return np.loadtxt(re.findall(r"\d", data), dtype=int).reshape(10, 10)


def step(octopi):
    octopi += 1

    flashed = np.zeros((10, 10), dtype=bool)
    while (flashing := ((octopi > 9) & ~flashed)).any():
        octopi += convolve(flashing.astype(int), KERNEL, mode="constant")
        flashed |= flashing

    octopi[flashed] = 0
    return flashed.sum()


def part_one(data):
    octopi = data.copy()
    return sum(step(octopi) for _ in range(100))


def part_two(data):
    octopi = data.copy()

    for s in itertools.count():
        if (octopi == 0).all():
            return s

        step(octopi)


def main():
    data = parse_data()

    print(f'Day 11 Part 01: {part_one(data)}')
    print(f'Day 11 Part 02: {part_two(data)}')
