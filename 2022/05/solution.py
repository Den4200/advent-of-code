from copy import deepcopy
import re

import numpy as np


def parse_data():
    with open("2022/05/input.txt") as f:
        data = f.read()

    sections = data.split("\n\n")
    crates = np.transpose([[line[i] for i in range(1, len(line), 4)] for line in sections[0].splitlines()[:-1]])[::,::-1]
    crates = [[crate for crate in stack if crate != " "] for stack in crates]
    moves = [tuple(map(int, re.findall("\d+", line))) for line in sections[1].splitlines()]

    return {
        "crates": crates,
        "moves": moves,
    }


def part_one(data):
    crates = deepcopy(data["crates"])
    moves = data["moves"]

    for move in moves:
        for _ in range(move[0]):
            crates[move[2] - 1].append(crates[move[1] - 1].pop())

    return "".join(stack[-1] for stack in crates)


def part_two(data):
    crates = data["crates"]
    moves = data["moves"]

    for move in moves:
        crates[move[2] - 1] += reversed([crates[move[1] - 1].pop() for _ in range(move[0])])

    return "".join(stack[-1] for stack in crates)


def main():
    data = parse_data()

    print(f"Day 05 Part 01: {part_one(data)}")
    print(f"Day 05 Part 02: {part_two(data)}")
