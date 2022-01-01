import numpy as np


def parse_data():
    with open('2021/25/input.txt') as f:
        data = f.read()

    return np.array([list(line) for line in data.splitlines()])


def step(seafloor):
    east_cucumbers = (seafloor == ">") & np.roll(seafloor == ".", -1, 1)
    seafloor[east_cucumbers] = "."
    seafloor[np.roll(east_cucumbers, 1, 1)] = ">"

    south_cucumbers = (seafloor == "v") & np.roll(seafloor == ".", -1, 0)
    seafloor[south_cucumbers] = "."
    seafloor[np.roll(south_cucumbers, 1, 0)] = "v"

    return (east_cucumbers | south_cucumbers).any()


def part_one(data):
    steps = 0

    while step(data):
        steps += 1

    return steps + 1


def part_two(data):
    pass


def main():
    data = parse_data()

    print(f'Day 25 Part 01: {part_one(data)}')
    print(f'Day 25 Part 02: {part_two(data)}')
