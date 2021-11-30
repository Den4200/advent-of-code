def parse_data():
    with open('2020/25/input.txt') as f:
        data = f.read()

    return [int(num) for num in data.splitlines()]


def calculate_loop_size(public_key):
    value = 1
    loop_size = 1

    while True:
        value = (value * 7) % 20201227

        if value == public_key:
            return loop_size
        else:
            loop_size += 1


def calculate_encryption_key(subject_number, loop_size):
    encryption_key = 1

    for _ in range(loop_size):
        encryption_key = (encryption_key * subject_number) % 20201227

    return encryption_key


def part_one(data):
    return calculate_encryption_key(
        data[0],
        calculate_loop_size(data[1])
    )


def part_two(data):
    pass


def main():
    data = parse_data()

    print(f'Day 25 Part 01: {part_one(data)}')
    print(f'Day 25 Part 02: {part_two(data)}')
