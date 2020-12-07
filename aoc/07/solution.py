import re
from functools import cache


def parse_data():
    with open('aoc/07/input.txt') as f:
        data = f.read()

    data = [
        (
            ' '.join(line.split()[:2]),
            re.findall(r'(\d) (\w+ \w+) bag', line)
        )
        for line in data.splitlines()
    ]

    return {
        line[0]: {part[1]: int(part[0]) for part in line[1]} for line in data
    }


def part_one(data):

    @cache
    def has_shiny_gold(bag):
        if 'shiny gold' in data[bag]:
            return True

        return any(has_shiny_gold(b) for b in data[bag])

    return sum(has_shiny_gold(bag) for bag in data)


def part_two(data):

    def count_bags(bag):
        return sum(count_bags(b) * amt for b, amt in data[bag].items()) + 1

    return count_bags('shiny gold') - 1


def main():
    data = parse_data()

    print(f'Day 07 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 07 Part 02: {part_two(data) or "skipped"}')
