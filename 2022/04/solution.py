def parse_data():
    with open("2022/04/input.txt") as f:
        data = f.read()

    return [
        [[int(n) for n in p.split("-")] for p in line.split(",")]
        for line in data.splitlines()
    ]


def part_one(data):
    return sum(
        p1[0] <= p2[0] and p1[1] >= p2[1] or p1[0] >= p2[0] and p1[1] <= p2[1]
        for p1, p2 in data
    )


def part_two(data):
    return sum(p1[0] <= p2[1] and p1[1] >= p2[0] for p1, p2 in data)


def main():
    data = parse_data()

    print(f"Day 04 Part 01: {part_one(data)}")
    print(f"Day 04 Part 02: {part_two(data)}")
