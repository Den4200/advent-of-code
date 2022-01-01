def parse_data():
    with open('2021/24/input.txt') as f:
        data = f.read().splitlines()

    div1 = []
    div26 = []

    for i in range(0, len(data), 18):
        if data[i + 4][-1] == "1":
            div1.append(int(data[i + 15].rsplit(maxsplit=1)[-1]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(data[i + 5].rsplit(maxsplit=1)[-1]))

    return div1, div26


def monad(div1, div26, mode):
    model = [0] * 14
    stack = []
    compare = min if mode == 9 else max

    for i, (y, x) in enumerate(zip(div1, div26)):
        if y is not None:
            stack.append((i, y))
        else:
            iy, y = stack.pop()
            delta = x + y

            model[iy] = compare(mode, mode - delta)
            model[i] = compare(mode, mode + delta)

    return "".join(str(digit) for digit in model)


def part_one(data):
    return monad(*data, 9)


def part_two(data):
    return monad(*data, 1)


def main():
    data = parse_data()

    print(f'Day 24 Part 01: {part_one(data)}')
    print(f'Day 24 Part 02: {part_two(data)}')
