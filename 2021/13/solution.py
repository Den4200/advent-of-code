import re

import numpy as np
from advent_of_code_ocr import convert_array_6


def parse_data():
    with open('2021/13/input.txt') as f:
        data = f.read()

    coords = np.array([(int(n1), int(n2)) for n1, n2 in re.findall(r"(\d+),(\d+)", data)], dtype=int)
    folds = [(axis, int(n)) for axis, n in re.findall(r"fold along (x|y)=(\d+)", data)]

    paper = np.zeros((coords[:, 1].max() + 1, coords[:, 0].max() + 1), dtype=bool)
    for x, y in coords:
        paper[y, x] = True

    return paper, folds


def fold(paper, axis, coord):
    if axis == "x":
        return paper[:, :coord] | paper[:, -1: coord: -1]
    elif axis == "y":
        return paper[:coord] | paper[-1: coord: -1]


def part_one(data):
    paper, folds = data
    return fold(paper, *folds[0]).sum()


def part_two(data):
    paper, folds = data

    for f in folds:
        paper = fold(paper, *f)

    # Visualize solution
    #
    # print("\n".join("".join("██" if coord else "  " for coord in row) for row in paper))
    #
    # import matplotlib.pyplot as plt
    # plt.imshow(paper)
    # plt.show()

    return convert_array_6(paper, fill_pixel=1, empty_pixel=0)


def main():
    data = parse_data()

    print(f'Day 13 Part 01: {part_one(data)}')
    print(f'Day 13 Part 02: {part_two(data)}')
