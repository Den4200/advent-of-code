import re


def parse_data():
    with open('aoc/08/input.txt') as f:
        data = f.read()

    return [re.fullmatch(r'([a-z]{3}) ((?:\+|-)\d+)', line).groups() for line in data.splitlines()]


def execute(data):
    acc = 0
    instructions = set()

    idx = 0
    while idx < len(data):
        action, value = data[idx]

        if action == 'acc':
            acc += int(value)
            idx += 1
        elif action == 'jmp':
            idx += int(value)
        else:
            idx += 1

        if idx not in instructions:
            instructions.add(idx)
        else:
            break

    return idx, acc


def part_one(data):
    return execute(data)[1]


def part_two(data):
    for i, instruction in enumerate(data):
        action, value = instruction

        if action == 'jmp':
            action = 'nop'

        elif action == 'nop':
            action = 'jmp'

        else:
            continue

        idx, acc = execute(data[:i] + [(action, value)] + data[i + 1:])

        if idx == len(data):
            return acc


def main():
    data = parse_data()

    print(f'Day 08 Part 01: {part_one(data)}')
    print(f'Day 08 Part 02: {part_two(data)}')
