from collections import defaultdict
from functools import reduce
import re


def parse_data():
    with open("2023/04/input.txt") as f:
        data = [line.split(":")[1].split("|") for line in f]

    return {
        card: len(
            reduce(
                lambda s1, s2: s2 if len(s1) == 0 else s1 & s2,
                ({int(num) for num in re.findall(r"(\d+)", part)} for part in line),
                set(),
            )
        )
        for card, line in enumerate(data, start=1)
    }


def part_one(data):
    return sum(2**wins // 2 for wins in data.values())


def part_two(data):
    cards = defaultdict(int)

    for card, wins in data.items():
        cards[card] += 1

        for new_card in range(card + 1, card + wins + 1):
            cards[new_card] += cards[card]

    return sum(cards.values())


def main():
    data = parse_data()

    print(f"Day 04 Part 01: {part_one(data)}")
    print(f"Day 04 Part 02: {part_two(data)}")
