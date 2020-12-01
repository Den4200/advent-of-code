#! /usr/bin/env python3

import importlib
import os
import sys
import typing as t
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

import requests

from aoc import YEAR


STARTING_CODE = """\
from aoc import submit


def parse_data(data):
    pass


def part_one(data):
    pass


def part_two(data):
    pass


def main():
    with open('{input_file}') as f:
        problem_input = f.read()

    data = parse_data(problem_input)

    answer_one = part_one(data)
    answer_two = part_two(data)

    print(f'Day {day:02} Part 01: {{answer_one or "skipped"}}')
    print(f'Day {day:02} Part 02: {{answer_two or "skipped"}}')

    submit({day}, 1, answer_one)
    submit({day}, 2, answer_two)
"""

AOC_SESSION_COOKIE = os.environ.get('AOC_SESSION_COOKIE')


def advent_day(day: str) -> int:
    day = int(day)

    if 1 <= day <= 25:
        return day
    
    raise ArgumentTypeError(f'{day} is not in range of 1 - 25')


def aoc_part(part: str) -> int:
    part = int(part)

    if part in (1, 2):
        return part

    raise ArgumentTypeError(f'{day} is not in range of 1 - 2')


def get_input(day: int) -> t.Optional[str]:
    if AOC_SESSION_COOKIE is None:
        raise ValueError('Missing AOC_SESSION_COOKIE!')

    problem_input = requests.get(
        f'https://adventofcode.com/{YEAR}/day/{day}/input',
        cookies={'session': AOC_SESSION_COOKIE}
    )

    if not problem_input.ok:
        raise ValueError(f'Bad response from site: {problem_input.status_code}')

    return problem_input.text


def create_day(day: int) -> None:
    problem_input = get_input(day)

    directory = Path('aoc') / f'{day:02}'
    directory.mkdir()

    input_file = directory / 'input.txt'
    input_file.write_text(problem_input)

    solution = directory / 'solution.py'
    solution.write_text(
        STARTING_CODE.format(
            input_file=input_file.relative_to('.'),
            day=day
        )
    )


def run_day(day: int) -> None:
    importlib.import_module(f'aoc.{day:02}.solution').main()


if __name__ == "__main__":
    parser = ArgumentParser(description='Advent of Code!')

    parser.add_argument('--create', '-c', action='store_true', help="Create the given day's workspace")
    parser.add_argument('--run', '-r', action='store_true', help="Run the given day's solution")
    parser.add_argument('day', type=advent_day, help='The day for the problem set')
    
    args = parser.parse_args()

    if args.create:
        create_day(args.day)

    if args.run:
        run_day(args.day)
