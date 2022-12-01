def parse_data():
    with open("2022/01/input.txt") as f:
        data = f.read()

    return [
        [int(line) for line in lines.splitlines()]
        for lines in data.split("\n\n")
    ]


def part_one(data):
    return max(sum(elf) for elf in data)


def part_two(data):
    return sum(sorted(sum(elf) for elf in data)[-3:])


def main():
    data = parse_data()

    print(f"Day 01 Part 01: {part_one(data)}")
    print(f"Day 01 Part 02: {part_two(data)}")
