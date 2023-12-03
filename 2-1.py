import re
from common.cli import get_input

max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

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
    game_id = re.match("^Game ([0-9]+)", game)[1]

    valid_game = True
    draws = parse_draws(game)
    for draw in draws:
        for color, count in max_colors.items():
            if color in draw and int(draw[color]) > count:
                valid_game = False
                break
    
    if valid_game:
        counter += int(game_id)

print(counter)
