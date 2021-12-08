def parse_data():
    with open('2021/08/input.txt') as f:
        data = f.read()

    signals = []
    outputs = []
    for line in data.splitlines():
        s, o = line.split("|")
        signals.append([set(signal) for signal in s.split()])
        outputs.append([set(output) for output in o.split()])

    return signals, outputs


def part_one(data):
    return sum(len(digit) in {2, 3, 4, 7} for line in data[1] for digit in line)


def part_two(data):
    decoder = {
        (2, 2, 2): 1,
        (3, 2, 2): 7,
        (4, 4, 2): 4,
        (7, 4, 2): 8,
        (5, 2, 1): 2,
        (5, 3, 1): 5,
        (5, 3, 2): 3,
        (6, 4, 2): 9,
        (6, 3, 1): 6,
        (6, 3, 2): 0,
    }

    output_sum = 0
    for signals, outputs in zip(*data):
        signal_map = {len(signal): signal for signal in signals}
        output_value = 0

        for output in outputs:
            output_value = output_value * 10 + decoder[
                len(output),
                len(output & signal_map[4]),
                len(output & signal_map[2]),
            ]

        output_sum += output_value

    return output_sum


def main():
    data = parse_data()

    print(f'Day 08 Part 01: {part_one(data)}')
    print(f'Day 08 Part 02: {part_two(data)}')
