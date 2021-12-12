import networkx as nx


def parse_data():
    with open('2021/12/input.txt') as f:
        data = f.read()

    return nx.Graph(line.split("-") for line in data.splitlines())


def part_one(data, cave="start", small_caves=()):
    if cave == "end":
        return 1

    if cave.islower():
        small_caves += (cave,)

    return sum(
        part_one(data, neighbor, small_caves)
        for neighbor in data[cave]
        if neighbor not in small_caves
    )


def part_two(data, cave="start", small_caves=(), seen_twice=None):
    if cave == "end":
        return 1

    if cave.islower():
        if cave not in small_caves:
            small_caves += (cave,)
        else:
            seen_twice = cave

    return sum(
        part_two(data, neighbor, small_caves, seen_twice)
        for neighbor in data[cave]
        if neighbor != "start" and (neighbor not in small_caves or seen_twice is None)
    )


def main():
    data = parse_data()

    print(f'Day 12 Part 01: {part_one(data)}')
    print(f'Day 12 Part 02: {part_two(data)}')
