import numpy as np


def parse_data():
    with open('2021/04/input.txt') as f:
        data = f.read().splitlines()

    draws = [int(draw) for draw in data[0].split(",")]
    boards = np.loadtxt(data[1:], dtype=int).reshape(-1, 5, 5)

    return draws, boards


def check_winners(boards):
    winning_rows = (boards == -42).all(1)
    winning_cols = (boards == -42).all(2)
    winners = (winning_rows | winning_cols).any(1)

    return winners


def part_one(data):
    draws, boards = data

    for draw in draws:
        boards[boards == draw] = -42  # The answer to life?
        winners = check_winners(boards)

        if winners.any():
            boards[boards == -42] = 0
            return boards[winners].sum() * draw


def part_two(data):
    draws, boards = data

    for draw in draws:
        boards[boards == draw] = -42
        winners = check_winners(boards)

        if winners.any():
            if len(boards) > 1:
                boards = boards[~winners]
            else:
                boards[boards == -42] = 0
                return boards.sum() * draw


def main():
    data = parse_data()

    print(f'Day 04 Part 01: {part_one(data)}')
    print(f'Day 04 Part 02: {part_two(data)}')
