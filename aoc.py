#!/usr/bin/env python3

import importlib
import os
import typing as t
import webbrowser
from argparse import ArgumentParser, ArgumentTypeError
from timeit import default_timer as timer
from pathlib import Path

import requests
from bs4 import BeautifulSoup


AOC_SESSION_COOKIE = os.environ.get('AOC_SESSION_COOKIE')
YEAR = 2020

STARTING_CODE = """\
def parse_data():
    with open('{input_file}') as f:
        data = f.read()


def part_one(data):
    pass


def part_two(data):
    pass


def main():
    data = parse_data()

    print(f'Day {day:02} Part 01: {{part_one(data)}}')
    print(f'Day {day:02} Part 02: {{part_two(data)}}')
"""


def advent_day(day: str) -> int:
    day = int(day)

    if 1 <= day <= 25:
        return day
    
    raise ArgumentTypeError(f'{day} is not in range of 1 - 25')


def aoc_part(part: str) -> int:
    part = int(part)

    if part in (1, 2):
        return part

    raise ArgumentTypeError(f'{part} is not in range of 1 - 2')


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

    directory = Path(str(YEAR)) / f'{day:02}'
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


def run_day(day: int, part: t.Optional[int]) -> None:
    solution_module = importlib.import_module(f'{YEAR}.{day:02}.solution')

    if part is None:
        solution_module.main()
    elif part == 1:
        print(solution_module.part_one(solution_module.parse_data()))
    elif part == 2:
        print(solution_module.part_two(solution_module.parse_data()))


def time_solution(day: int, part: int) -> None:
    solution_module = importlib.import_module(f'{YEAR}.{day:02}.solution')
    data = solution_module.parse_data()

    if part == 1:
        action = solution_module.part_one
    else:
        action = solution_module.part_two

    start = timer()
    answer = action(data)
    end = timer()

    print(f'Day {day:02} Part {part:02}: {answer}')
    print(f'Time elapsed: {end - start:.10f}')


def time_solutions(day: int, part: t.Optional[int]) -> None:
    if part is None:
        time_solution(day, 1)
        print()
        time_solution(day, 2)

    else:
        time_solution(day, part)


def visualize_solution(day: int) -> None:
    try:
        visualization_module = importlib.import_module(f'{YEAR}.{day:02}.visualization')
    except ImportError:
        print(f'Visualization not found for day {day}')
        return

    visualization_module.main()


def submit(day: int, part: int) -> None:
    if AOC_SESSION_COOKIE is None:
        raise ValueError('Missing AOC_SESSION_COOKIE!')

    part_word = 'one' if part == 1 else 'two'

    solution_module = importlib.import_module(f'{YEAR}.{day:02}.solution')
    answer_func = getattr(solution_module, f'part_{part_word}')
    problem_input = getattr(solution_module, 'parse_data')()

    answer = answer_func(problem_input)

    resp = requests.post(
        f'https://adventofcode.com/{YEAR}/day/{day}/answer',
        cookies={'session': AOC_SESSION_COOKIE},
        data={'level': part, 'answer': answer}
    )

    if not resp.ok:
        raise ValueError(f'Bad response from site: {resp.status_code}')

    msg = BeautifulSoup(resp.text, 'html.parser').article.text

    if msg.startswith("That's the") and part == 1:
        webbrowser.open(resp.url)
    
    print(f'Day {day:02} Part {part:02}: {msg}')


def main():
    parser = ArgumentParser(description='Advent of Code!')

    parser.add_argument('-c', '--create', action='store_true', help="create the given day's workspace")
    parser.add_argument('-r', '--run', action='store_true', help="run the given day's solution")
    parser.add_argument('-t', '--timeit', action='store_true', help="time the given day's solution")
    parser.add_argument('-v', '--visualize', action='store_true', help="visualize the given day's solution")
    parser.add_argument('-s', '--submit', action='store_true', help="submit the given day's solution")

    parser.add_argument('day', type=advent_day, help='the day for the problem set')
    parser.add_argument('part', type=aoc_part, nargs='?', help='the part of the problem set')

    args = parser.parse_args()

    if args.create:
        create_day(args.day)

    if args.run:
        run_day(args.day, args.part)

    if args.timeit:
        time_solutions(args.day, args.part)

    if args.visualize:
        visualize_solution(args.day)

    if args.submit:
        if args.part is None:
            parser.error('the following arguments are required: part')
        else:
            submit(args.day, args.part)


if __name__ == "__main__":
    main()
