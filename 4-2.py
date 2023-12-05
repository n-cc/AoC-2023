import re

from common.cli import get_input

card_dict = {}

def get_winning_cards(id):
    c = 0
    score = 1

    for n in card_dict[id]["ours"]:
        if n in card_dict[id]["winning"]:
            c += 1

    for i in range(1, c + 1):
        score += get_winning_cards(id + i)

    return score

for card in get_input():
    num = re.match("^Card +([0-9]+).*", card)[1]
    winning = [n for n in re.match(".*: ([0-9 ]+)\|.*", card)[1].strip().split(" ") if n]
    ours = [n for n in re.match(".*\|([0-9 ]+).*", card)[1].strip().split(" ") if n]

    card_dict[int(num)] = { "winning": winning, "ours": ours}


print(sum([get_winning_cards(n) for n in card_dict.keys()]))