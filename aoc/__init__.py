import os

import requests
import webbrowser
from bs4 import BeautifulSoup

AOC_SESSION_COOKIE = os.environ.get('AOC_SESSION_COOKIE')
YEAR = 2020


def submit(day, part, answer):
    if AOC_SESSION_COOKIE is None or answer is None:
        return

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
