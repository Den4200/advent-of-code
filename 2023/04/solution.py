from collections import defaultdict
import re


def parse_data():
    with open("2023/04/input.txt") as f:
        data = [line.split(":")[1].split("|") for line in f]

    return {
        card: [{int(num) for num in re.findall(r"(\d+)", part)} for part in line]
        for card, line in enumerate(data, start=1)
    }


def part_one(data):
    return sum(2 ** len(winning & nums) // 2 for winning, nums in data.values())


def part_two(data):
    cards = defaultdict(int)

    for card, (winning, nums) in data.items():
        cards[card] += 1

        for new_card in range(card + 1, card + len(winning & nums) + 1):
            cards[new_card] += cards[card]

    return sum(cards.values())


def main():
    data = parse_data()

    print(f"Day 04 Part 01: {part_one(data)}")
    print(f"Day 04 Part 02: {part_two(data)}")
