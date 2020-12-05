def parse_data():
    with open('aoc/05/input.txt') as f:
        data = f.read()

    return data.splitlines()


def get_ids(data):
    to_binary = str.maketrans('FBLR', '0101')
    return [int(code.translate(to_binary), base=2) for code in data]


def part_one(data):
    return max(get_ids(data))


def part_two(data):
    ids = get_ids(data)

    min_id = min(ids)
    max_id = max(ids)

    seats_available = (max_id * (max_id + 1) - min_id * (min_id - 1)) // 2
    seats_occupied = sum(ids)

    return seats_available - seats_occupied

def main():
    data = parse_data()

    print(f'Day 05 Part 01: {part_one(data) or "skipped"}')
    print(f'Day 05 Part 02: {part_two(data) or "skipped"}')
