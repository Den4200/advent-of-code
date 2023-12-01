import re

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def parse_data():
    with open("2023/01/input.txt") as f:
        return f.readlines()


def find_digit(line, reverse=False):
    if reverse:
        line = "".join(reversed(line))

    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        for num, val in NUMBERS.items():
            if reverse:
                num = "".join(reversed(num))

            if line[i:min(i + len(num), len(line))] == num:
                return val


def part_one(data):
    return sum(int((n := re.findall(r"(\d)", line))[0] + n[-1]) for line in data)


def part_two(data):
    return sum(int(find_digit(line) + find_digit(line, reverse=True)) for line in data)


def main():
    data = parse_data()

    print(f"Day 01 Part 01: {part_one(data)}")
    print(f"Day 01 Part 02: {part_two(data)}")
