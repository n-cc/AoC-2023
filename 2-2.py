from functools import reduce

from common.cli import get_input

def parse_draws(game: str) -> list:
    draws = []
    for draw in game.split(": ")[1:][0].split("; "):
        d = {}
        for entry in draw.split(", "):
            count, color = entry.split(" ")
            d[color] = count
        draws.append(d)

    return draws

counter = 0

for game in get_input():
    draws = parse_draws(game)

    counts = {
        "blue": 1,
        "green": 1,
        "red": 1,
    }

    for draw in draws:
        for color, count in draw.items():
            count = int(count)
            if count > counts[color]:
                counts[color] = count

    counter += reduce(lambda x, y: x * y, counts.values())

print(counter)
