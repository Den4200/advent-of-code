import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

BIN_POWERS = 2 ** np.arange(8, -1, -1).reshape(3, 3)


def parse_data():
    with open('2021/20/input.txt') as f:
        data = f.read().splitlines()

    algo = np.array([px == "#" for px in data[0]], dtype=int)
    image = np.array([[px == "#" for px in line] for line in data[2:]], dtype=int)
    return algo, image


def enhance(x, algo, image):
    image = np.pad(image, 2 * x)

    for _ in range(x):
        window = sliding_window_view(image, (3, 3))
        image = algo[(window * BIN_POWERS).sum((3, 2))]

    return image


def part_one(data):
    return np.count_nonzero(enhance(2, *data))


def part_two(data):
    return np.count_nonzero(enhance(50, *data))


def main():
    data = parse_data()

    print(f'Day 20 Part 01: {part_one(data)}')
    print(f'Day 20 Part 02: {part_two(data)}')
