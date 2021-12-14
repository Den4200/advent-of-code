import re
from collections import Counter


def parse_data():
    with open('2021/14/input.txt') as f:
        data = f.read()

    polymer_template = list(data.split(maxsplit=1)[0])
    pair_insertions = dict(re.findall(r"([A-Z]{2}) -> ([A-Z])", data))

    return polymer_template, pair_insertions


def npolymers(polymers, pair_insertions, steps):
    pair_count = Counter("".join(pair) for pair in zip(polymers, polymers[1:]))

    for _ in range(steps):
        new_pair_count = Counter()
        for pair in pair_count:
            new_pair_count[pair[0] + pair_insertions[pair]] += pair_count[pair]
            new_pair_count[pair_insertions[pair] + pair[1]] += pair_count[pair]

        pair_count = new_pair_count

    polymer_counts = Counter()
    for pair in pair_count:
        polymer_counts[pair[0]] += pair_count[pair]

    polymer_counts[polymers[-1]] += 1
    sorted_counts = polymer_counts.most_common()
    return sorted_counts[0][1] - sorted_counts[-1][1]


def part_one(data):
    return npolymers(*data, 10)


def part_two(data):
    return npolymers(*data, 40)


def main():
    data = parse_data()

    print(f'Day 14 Part 01: {part_one(data)}')
    print(f'Day 14 Part 02: {part_two(data)}')
