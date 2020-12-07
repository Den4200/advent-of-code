import re


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


def has_shiny_gold(bag, data):
    if 'shiny gold' in data[bag]:
        return True

    return any(has_shiny_gold(b, data) for b in data[bag])


def count_bags(bag, data):
    return sum(count_bags(b, data) * amt for b, amt in data[bag].items()) + 1


def part_one(data):
    return sum(has_shiny_gold(bag, data) for bag in data)


def part_two(data):
    return count_bags('shiny gold', data) - 1


def main():
    data = parse_data()

    print(f'Day 07 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 07 Part 02: {part_two(data) or "skipped"}')
