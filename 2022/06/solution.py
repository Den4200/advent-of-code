from numpy.lib.stride_tricks import sliding_window_view


def parse_data():
    with open("2022/06/input.txt") as f:
        data = f.read()

    return list(data.strip())


def part_one(data):
    for i, chars in enumerate(sliding_window_view(data, 4)):
        if len(set(chars)) == 4:
            return i + 4


def part_two(data):
    for i, chars in enumerate(sliding_window_view(data, 14)):
        if len(set(chars)) == 14:
            return i + 14


def main():
    data = parse_data()

    print(f"Day 06 Part 01: {part_one(data)}")
    print(f"Day 06 Part 02: {part_two(data)}")
