from collections import Counter


def parse_data():
    with open('2018/02/input.txt') as f:
        data = f.read()

    return data.splitlines()


def part_one(data):
    twos = 0
    threes = 0

    for id_ in data:
        chars = Counter(id_)
        twos += any(count == 2 for count in chars.values())
        threes += any(count == 3 for count in chars.values())

    return twos * threes


def part_two(data):
    for idx, id_ in enumerate(data[:-1]):
        for comparison in data[idx+1:]:
            diff = []

            for pos, pair in enumerate(zip(id_, comparison)):
                if pair[0] != pair[1]:
                    diff.append(pos)

                    if len(diff) > 1:
                        break

            if len(diff) == 1:
                return id_[:diff[0]] + id_[diff[0] + 1:]


def main():
    data = parse_data()

    print(f'Day 02 Part 01: {part_one(data)}')
    print(f'Day 02 Part 02: {part_two(data)}')
