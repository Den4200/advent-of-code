from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from typing import Callable, NamedTuple


class Operation(Enum):
    ACC = 'acc'
    JMP = 'jmp'
    NOP = 'nop'

    @staticmethod
    def acc(app: Application):
        app.accumulator += app.instructions[app.pointer].argument
        app.pointer += 1

    @staticmethod
    def jmp(app: Application):
        app.pointer += app.instructions[app.pointer].argument

    @staticmethod
    def nop(app: Application):
        app.pointer += 1


class Instruction(NamedTuple):
    operation: Operation
    argument: int

    @classmethod
    def from_line(cls, line: str) -> Instruction:
        match = re.fullmatch(r'([a-z]{3}) ((?:\+|-)\d+)', line)
        return cls(Operation(match[1]), int(match[2]))


@dataclass
class Application:
    instructions: list[Instruction]
    accumulator: int = 0
    pointer: int = 0

    def __enter__(self) -> Application:
        self.__previous_instructions = self.instructions.copy()
        self.__previous_accumulator = self.accumulator
        self.__previous_pointer = self.pointer
        return self

    def __exit__(self, type, value, traceback):
        self.instructions = self.__previous_instructions
        self.accumulator = self.__previous_accumulator
        self.pointer = self.__previous_pointer

    @classmethod
    def from_lines(cls, lines: list[str]) -> Application:
        return cls([
            Instruction.from_line(line) for line in lines
        ])

    def step(self) -> Instruction:
        instruction = self.instructions[self.pointer]

        if action := getattr(Operation, instruction.operation.value):
            action(self)
        else:
            raise ValueError(f'Invalid operation at instruction {self.pointer}')

        return Instruction

    def execute(self):
        instructions = set()

        while self.pointer < len(self.instructions):
            instruction = self.step()

            if self.pointer in instructions:
                break

            instructions.add(self.pointer)


def parse_data():
    with open('aoc/08/input.txt') as f:
        data = f.read()

    return Application.from_lines(data.splitlines())


def part_one(app: Application) -> int:
    with app:
        app.execute()
        return app.accumulator


def part_two(app: Application) -> int:
    for index, instruction in enumerate(app.instructions):
        op, arg = instruction

        if op is Operation.JMP:
            op = Operation.NOP

        elif op is Operation.NOP:
            op = Operation.JMP

        else:
            continue

        with app:
            app.instructions[index] = Instruction(op, arg)
            app.execute()

            if app.pointer == len(app.instructions):
                return app.accumulator


def main():
    data = parse_data()

    print(f'Day 08 Part 01: {part_one(data)}')
    print(f'Day 08 Part 02: {part_two(data)}')
