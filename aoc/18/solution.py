import contextlib
import operator
import re


OPERATIONS = {
    '*': operator.mul,
    '/': operator.truediv,
    '+': operator.add,
    '-': operator.sub
}


def parse_data():
    with open('aoc/18/input.txt') as f:
        data = f.read()

    return [[char for char in line if char != ' '] for line in data.splitlines()]


def parse_expr(expr):
    nums = re.findall(r'(\d+)', expr)
    ops = re.findall(r'(\*|\/|\+|\-)', expr)

    return nums, ops


def sub_expr(expr):
    with contextlib.suppress(ValueError):
        left = len(expr) - expr[::-1].index('(') - 1

        for i in range(left + 1, len(expr)):
            if expr[i] == ')':
                return left, i


def solve(expr):
    nums, ops = parse_expr(''.join(expr))

    answer = int(nums.pop(0))
    for op, num in zip(ops, nums):
        answer = OPERATIONS[op](answer, int(num))

    return answer


def solve_high_add_precedence(expr):
    nums, ops = parse_expr(''.join(expr))

    result = [nums.pop(0)]

    for op, num in zip(ops, nums):
        if op == '+':
            result.append(str(int(result.pop(-1)) + int(num)))
        else:
            result.extend((op, num))

    return result


def part_one(data):
    answers = list()

    for expr in data:
        while (idxs := sub_expr(expr)):
            left, right = idxs
            expr[left:right + 1] = (str(solve(expr[left + 1:right])),)

        answers.append(solve(expr))

    return sum(answers)


def part_two(data):
    answers = list()

    for expr in data:
        while (idxs := sub_expr(expr)):
            left, right = idxs
            expr[left:right + 1] = (
                str(solve(solve_high_add_precedence(expr[left + 1:right]))),
            )

        answers.append(solve(solve_high_add_precedence(expr)))

    return sum(answers)


def main():
    data = parse_data()

    print(f'Day 18 Part 01: {part_one(data)}')
    print(f'Day 18 Part 02: {part_two(data)}')
