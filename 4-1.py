import re

from common.cli import get_input

def parse_card(card: str) -> int:
    c = 0
    winning = [n for n in re.match(".*: ([0-9 ]+)\|.*", card)[1].strip().split(" ") if n]
    ours = [n for n in re.match(".*\|([0-9 ]+).*", card)[1].strip().split(" ") if n]

    for n in ours:
        if n in winning:
            c += 1

    if c:
        return pow(2, c - 1)
    else:
        return 0

print(sum([parse_card(card) for card in get_input()]))