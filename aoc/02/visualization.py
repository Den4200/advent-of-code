import curses
import re
import time
from collections import deque


def parse_data():
    with open('aoc/02/input.txt') as f:
        data = f.read()

    return list(re.findall(r'(\d+)-(\d+) (\w): (\w+)', data))


class SubWindow:

    def __init__(self, stdscr, height, width, x, y):
        self.stdscr = stdscr

        self.height = height
        self.width = width

        self.center_height = height // 2
        self.center_width = width // 2

        self.x = x
        self.y = y

        self.center_x = x + self.center_width
        self.center_y = y + self.center_height

        self.subwin = stdscr.subwin(height, width, x , y)

    def __getattr__(self, attr):
        if (value := getattr(self.subwin, attr)) is not None:
            return value

        raise AttributeError(f'{type(self.subwin)!r} object has no attribute {attr!r}')

    def center_text(self, text, *args, **kwargs):
        spacing = ' ' * (self.center_width - len(text) // 2)
        self.addstr(f'\n{spacing}{text}', *args, **kwargs)


def app(stdscr):
    curses.curs_set(0)
    
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1);

    height, width = stdscr.getmaxyx()

    data = parse_data()

    header = SubWindow(stdscr, 4, width - 2, 0, width // 2 - (width - 2) // 2)

    header.center_text('Advent of Code', curses.color_pair(2))
    header.center_text('Day 02 — Part 1', curses.color_pair(7))

    header.border(0)
    header.refresh()

    table = SubWindow(
        stdscr,
        height - 8,
        width - 2,
        height // 2 - (height - 8) // 2,
        width // 2 - (width - 2) // 2
    )

    table_headers = [
        'Letter',
        'Password',
        'Occurences',
        'Valid'
    ]

    col = table.width // len(table_headers)

    table_header = '\n'
    for header in table_headers:
        cell_margin = ' ' * ((col - len(header)) // 2)
        table_header += f'{cell_margin}{header}{cell_margin}'

    table_header += '\n\n'
    table.addstr(table_header)

    table.border(0)
    table.refresh()

    footer = SubWindow(
        stdscr,
        3,
        width - 2,
        height - 4,
        width // 2 - (width - 2) // 2
    )

    footer_starters = [
        'Total: 0',
        'Valid: 0',
        'Invalid: 0'
    ]

    footer_col = table.width // len(footer_starters)
    footer_text = '\n'
    for text in footer_starters:
        cell_margin = ' '  * ((footer_col - len(text)) // 2)
        footer_text += f'{cell_margin}{text}{cell_margin}'

    footer.addstr(footer_text)

    footer.border(0)
    footer.refresh()

    valid_pws = 0
    invalid_pws = 0

    table_buffer = deque()
    reached_max = False
    for lower, upper, letter, pw in data:
        time.sleep(0.25)

        if reached_max:
            table_buffer.popleft()

        elif len(table_buffer) > table.height - 4:
            table_buffer.popleft()
            reached_max = True

        chart_scale = (col - 4) / len(pw)

        lower = int(lower)
        upper = int(upper)
        count = pw.count(letter)

        occurences = list(f'[{"." * (col - 4)}]')
        occurences[int(lower * chart_scale)] = '>'
        occurences[int(upper * chart_scale)] = '<'

        if count > 0:
            occurences[int(count * chart_scale)] = '|'

        occur_margin = ' ' * ((col - len(occurences)) // 2)
        occurences[0] = f'{occur_margin}{occurences[0]}'
        occurences[-1] = f'{occurences[-1]}{occur_margin}'

        valid = lower <= count <= upper

        if valid:
            valid_pws += 1
        else:
            invalid_pws += 1

        line_buffer = list()

        line = ''
        for value in (letter, pw):
            cell_margin = ' ' * ((col - len(value)) // 2)

            text = f'{cell_margin}{value}{cell_margin}'
            text += ' ' * (col - len(text))

            line += text

        line_buffer.append((line, None))

        for char in occurences:
            if char in ('<', '>'):
                part = (char, curses.color_pair(1))
            elif char == '|':
                part = (char, curses.color_pair(4))
            else:
                part = (char, None)

            line_buffer.append(part)

        if valid:
            valid_text = 'valid'
            valid_color = curses.color_pair(2)
        else:
            valid_text = 'invalid'
            valid_color = curses.color_pair(1)

        valid_margin = ' ' * ((col - len(valid_text)) // 2)
        valid_text = f'{valid_margin}{valid_text}{valid_margin}'

        line_buffer.append((valid_text, valid_color))
        table_buffer.append(line_buffer)

        for idx, line in enumerate(table_buffer, start=3):
            last = 0

            for text, color in line:
                if color is not None:
                    table.addstr(idx, last, text, color)
                else:
                    table.addstr(idx, last, text)

                last += len(text)

        table.border(0)
        table.refresh()

        footer_values = [
            f'Total: {valid_pws + invalid_pws}',
            f'Valid: {valid_pws}',
            f'Invalid: {invalid_pws}'
        ]

        footer_text = ''
        for text in footer_values:
            cell_margin = ' '  * ((footer_col - len(text)) // 2)
            footer_text += f'{cell_margin}{text}{cell_margin}'

        footer.addstr(1, 0, footer_text)

        footer.border(0)
        footer.refresh()

    stdscr.getkey()


def main():
    curses.wrapper(app)
