def parse_data():
    with open("2022/25/input.txt") as f:
        data = f.read()

    return data.splitlines()


SNAFU_TO_DECIMAL = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2,
}

DECIMAL_TO_SNAFU = {
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
    5: "0",
}


def snafu_to_decimal(snafu_number):
    decimal = 0
    place = 1

    for n in reversed(snafu_number):
        decimal += SNAFU_TO_DECIMAL[n] * place
        place *= 5

    return decimal


def decimal_to_snafu(decimal_number):
    raw_digits = []
    while decimal_number != 0:
        decimal_number, remainder = divmod(decimal_number, 5)
        raw_digits.append(remainder)

    digits = []
    for place, digit in enumerate(raw_digits):
        digits.append(DECIMAL_TO_SNAFU[digit])

        if digit > 2:
            raw_digits[place + 1] += 1

    return "".join(reversed(digits))


def part_one(data):
    total = sum(snafu_to_decimal(snafu) for snafu in data)
    return decimal_to_snafu(total)


def part_two(data):
    pass


def main():
    data = parse_data()

    print(f"Day 25 Part 01: {part_one(data)}")
    print(f"Day 25 Part 02: {part_two(data)}")
