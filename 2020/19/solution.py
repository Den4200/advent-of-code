import re
from functools import cache


def parse_data():
    with open('2020/19/input.txt') as f:
        data = f.read()

    data = data.split('\n\n')

    rules = {(s := line.split(': '))[0]: s[1] for line in data[0].splitlines()}

    return rules, data[1].splitlines()


def part_one(data):
    rules = data[0]

    @cache
    def generate_regex(idx='0', max_depth=20):
        if max_depth == 0:
            return ''

        rule = rules[idx]

        if '|' in rule:
            left, right = rule.split(' | ')

            left = ''.join(generate_regex(num, max_depth - 1) for num in left.split())
            right = ''.join(generate_regex(num, max_depth - 1) for num in right.split())

            return f'({left}|{right})'

        elif match := re.fullmatch(r'"([a-z])"', rule):
            return match[1]

        else:
            return ''.join(generate_regex(num, max_depth - 1) for num in rule.split())

    regex = generate_regex()
    return sum(bool(re.fullmatch(regex, line)) for line in data[1])


def part_two(data):
    data[0]['8'] = '42 | 42 8'
    data[0]['11'] = '42 31 | 42 11 31'

    return part_one(data)


def main():
    data = parse_data()

    print(f'Day 19 Part 01: {part_one(data)}')
    print(f'Day 19 Part 02: {part_two(data)}')
