import re


def parse_data():
    with open('2020/04/input.txt') as f:
        data = f.read()

    return [
        dict(x.split(':') for x in line.split()) for line in data.split('\n\n')
    ]


def part_one(data):
    fields = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )

    needed = len(fields)
    valid = 0
    for passport in data:
        has = 0

        for field in fields:
            if passport.get(field) is not None:
                has += 1

        if has == needed:
            valid += 1

    return valid


def part_two(data):
    fields = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: (v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76),
        'hcl': lambda v: bool(re.fullmatch(r'#[0-9a-f]{6}', v)),
        'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda v: v.isdigit() and len(v) == 9,
    }

    needed = len(fields)
    valid = 0
    for passport in data:
        has = 0

        for field, validator in fields.items():
            if (v := passport.get(field)) is not None and validator(v):
                has += 1

        if has == needed:
            valid += 1

    return valid


def main():
    data = parse_data()

    print(f'Day 04 Part 01: {part_one(data)}')
    print(f'Day 04 Part 02: {part_two(data)}')
