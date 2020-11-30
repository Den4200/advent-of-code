#! /usr/bin/env python3

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
import os
import sys
import typing as t

import requests


YEAR = 2020
STARTING_CODE = """\
def part_one(data):
    pass


def part_two(data):
    pass


if __name__ == '__main__':
    with open('{input_file}') as f:
        problem_input = f.read()

    part_one(problem_input)
    part_two(problem_input)
"""


def advent_day(day: str) -> int:
    day = int(day)

    if 1 <= day <= 25:
        return day
    
    raise ArgumentTypeError(f'{day} is not in range of 1 - 25')


def get_input(day: int) -> t.Optional[str]:
    if (session_cookie := os.environ.get('AOC_SESSION_COOKIE')) is not None:
        problem_input = requests.get(
            f'https://adventofcode.com/{YEAR}/day/{day}/input',
            cookies={'session': session_cookie}
        )
        return problem_input.text


def create_day(day: int, problem_input: str) -> None:
    directory = Path('aoc') / f'{day:02}'
    directory.mkdir()

    input_file = directory / 'input.txt'
    input_file.write_text(problem_input)

    solution = directory / 'solution.py'
    solution.write_text(STARTING_CODE.format(input_file=input_file.relative_to('.')))


if __name__ == "__main__":
    parser = ArgumentParser(description='Get input for an Advent of Code 2020 problem.')
    parser.add_argument('day', type=advent_day, help='The day for the problem set.')

    day = parser.parse_args().day

    problem_input = get_input(day)
    if problem_input is None:
        print('Could not get problem input')
        sys.exit()

    create_day(day, problem_input)
