from functools import cache
from itertools import product


def parse_data():
    with open('2021/21/input.txt') as f:
        data = f.read()

    return [int(line.rsplit(maxsplit=1)[1]) for line in data.splitlines()]


def part_one(data):
    data = data.copy()
    scores = [0, 0]
    pi = 1
    rolls = 0

    def roll():
        nonlocal rolls
        rolls += 1
        return (rolls - 1) % 100 + 1

    while True:
        pi ^= 1
        data[pi] += sum(roll() for _ in range(3))
        data[pi] = (data[pi] - 1) % 10 + 1
        scores[pi] += data[pi]

        if scores[pi] >= 1000:
            return rolls * scores[pi ^ 1]


def part_two(data):

    @cache
    def dirac_dice(p1, p2, s1=0, s2=0):
        wins = [0, 0]

        for rolls in product((1, 2, 3), repeat=3):
            new_p1 = (p1 + sum(rolls) - 1) % 10 + 1
            new_s1 = s1 + new_p1

            if new_s1 >= 21:
                wins[0] += 1
            else:
                dp2, dp1 = dirac_dice(p2, new_p1, s2, new_s1)
                wins[0] += dp1
                wins[1] += dp2

        return wins

    return max(dirac_dice(*data.copy()))


def main():
    data = parse_data()

    print(f'Day 21 Part 01: {part_one(data)}')
    print(f'Day 21 Part 02: {part_two(data)}')
