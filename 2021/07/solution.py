import numpy as np
from scipy.optimize import minimize_scalar


def parse_data():
    with open('2021/07/input.txt') as f:
        data = f.read()

    return np.loadtxt([data], delimiter=",", dtype=int)


def part_one(data):
    return minimize_scalar(lambda x: np.abs(round(x) - data).sum()).fun


def part_two(data):
    return minimize_scalar(lambda x: (np.abs(round(x) - data) * (np.abs(round(x) - data) + 1) // 2).sum()).fun


def main():
    data = parse_data()

    print(f'Day 07 Part 01: {part_one(data)}')
    print(f'Day 07 Part 02: {part_two(data)}')
