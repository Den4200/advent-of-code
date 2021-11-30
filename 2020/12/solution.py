from math import cos, sin, radians


def parse_data():
    with open('2020/12/input.txt') as f:
        data = f.read()

    return [(line[0], int(line[1:])) for line in data.splitlines()]


def part_one(data):
    CARDINALS = {
        'E': 0,
        'N': 90,
        'W': 180,
        'S': 270,
    }

    position = [0, 0]
    current_angle = 0

    for dir_, amt in data:
        if dir_ in CARDINALS:
            rads = radians(CARDINALS[dir_])

            position[0] += round(cos(rads) * amt)
            position[1] += round(sin(rads) * amt)

        elif dir_ in ('L', 'R'):
            i = 1 if dir_ == 'L' else -1
            current_angle += radians(amt) * i

        elif dir_ == 'F':
            position[0] += round(cos(current_angle) * amt)
            position[1] += round(sin(current_angle) * amt)

    return abs(position[0]) + abs(position[1])


def part_two(data):
    CARDINALS = {
        'E': 0,
        'N': 90,
        'W': 180,
        'S': 270,
    }

    waypoint = [10, 1]
    position = [0, 0]

    for dir_, amt in data:
        if dir_ in CARDINALS:
            rads = radians(CARDINALS[dir_])

            waypoint[0] += round(cos(rads)) * amt
            waypoint[1] += round(sin(rads)) * amt

        elif dir_ in ('L', 'R'):
            i = 1 if dir_ == 'L' else -1
            rads = radians(amt) * i

            x, y = waypoint

            waypoint = [
                round(x * cos(rads) - y * sin(rads)),
                round(y * cos(rads) + x * sin(rads))
            ]

        elif dir_ == 'F':
            position[0] += waypoint[0] * amt
            position[1] += waypoint[1] * amt

    return abs(position[0]) + abs(position[1])


def main():
    data = parse_data()

    print(f'Day 12 Part 01: {part_one(data)}')
    print(f'Day 12 Part 02: {part_two(data)}')
