from copy import deepcopy
from dataclasses import dataclass
from math import prod
import operator
import re
from typing import Callable


OPERATIONS = {
    "*": operator.mul,
    "+": operator.add,
}


@dataclass
class Monkey:
    number: int
    items: list[int]
    operation: Callable
    operation_value: int | str
    divisor: int
    true_result: int
    false_result: int
    inspection_count: int

    def inspect(self):
        self.inspection_count += 1
        item = self.items.pop(0)

        return self.operation(
            item if self.operation_value == "old" else int(self.operation_value),
            item,
        ) // 3

    def inspect_with_worries(self, divisor):
        self.inspection_count += 1
        item = self.items.pop(0)

        return self.operation(
            item if self.operation_value == "old" else int(self.operation_value),
            item,
        ) % divisor


def parse_data():
    with open("2022/11/input.txt") as f:
        data = f.read()

    return [
        Monkey(
            int(monkey[0]),
            [int(item) for item in monkey[1].split(", ")],
            OPERATIONS[monkey[2]],
            monkey[3],
            int(monkey[4]),
            int(monkey[5]),
            int(monkey[6]),
            0,
        )
        for monkey in re.findall(
            r"Monkey (\d+):\n  Starting items: (.+)\n  Operation: new = old (\*|\+) (old|\d+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)",
            data
        )
    ]


def simulate_monkey_inspections(monkeys, rounds, inspector=None):
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.inspect() if inspector is None else inspector(monkey)
                to_throw = monkey.true_result if item % monkey.divisor == 0 else monkey.false_result

                monkeys[to_throw].items.append(item)

    monkeys.sort(key=lambda monkey: monkey.inspection_count, reverse=True)
    return monkeys[0].inspection_count * monkeys[1].inspection_count


def part_one(data):
    monkeys = deepcopy(data)
    return simulate_monkey_inspections(monkeys, 20)


def part_two(data):
    divisor = prod(monkey.divisor for monkey in data)
    return simulate_monkey_inspections(
        data,
        10_000,
        inspector=lambda monkey: monkey.inspect_with_worries(divisor)
    )


def main():
    data = parse_data()

    print(f"Day 11 Part 01: {part_one(data)}")
    print(f"Day 11 Part 02: {part_two(data)}")
