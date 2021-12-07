import numpy as np


def parse_data():
    with open('2021/07/input.txt') as f:
        data = f.read()

    return np.loadtxt([data], delimiter=",", dtype=int)


def part_one(data):
    median = np.median(data).astype(int)
    return np.abs(median - data).sum()


def part_two(data):
    mean = np.mean(data).astype(int)

    # We only need to account for mean +/- 0.5, but we need integers!
    bounds = np.arange(mean - 1, mean + 2)

    diff = np.abs(data - bounds[:, None])
    return (diff * (diff + 1) // 2).sum(1).min()


def main():
    data = parse_data()

    print(f'Day 07 Part 01: {part_one(data)}')
    print(f'Day 07 Part 02: {part_two(data)}')
