def parse_data():
    with open("2022/10/input.txt") as f:
        data = f.read()

    return [
        (parts[0], int(parts[1]))
        if (parts := line.split())[0] != "noop" else (parts[0], None)
        for line in data.splitlines()
    ]


def part_one(data):
    x = 1
    t = 0
    signal = 0

    def tick():
        nonlocal t, signal

        t += 1
        if t in (20, 60, 100, 140, 180, 220):
            signal += t * x

    for operation in data:
        match operation:
            case ["addx", value]:
                tick()
                tick()
                x += value
            case ["noop", None]:
                tick()

    return signal


def part_two(data):
    x = 1
    t = 0

    def tick():
        nonlocal t

        if t % 40 in (x - 1, x, x + 1):
            print("#", end="")
        else:
            print(".", end="")

        t += 1
        if t % 40 == 0:
            print()

    for operation in data:
        match operation:
            case ["addx", value]:
                tick()
                tick()
                x += value
            case ["noop", None]:
                tick()

    print()


def main():
    data = parse_data()

    print(f"Day 10 Part 01: {part_one(data)}")
    print(f"Day 10 Part 02: {part_two(data)}")
