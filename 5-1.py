import re
from collections import OrderedDict
from common.cli import get_input

def get_next(value, maps):
    for m in maps:
        transform = m['src'] - m['dest']
        if m['src'] <= value <= m['src'] + m['length']:
            return value - transform
    return value

seeds = []
maps = OrderedDict()

map_type = ""

for line in get_input():
    map_seeds = re.match("^seeds:.*", line)
    map_start = re.match("^([A-Za-z-]+) map:$", line)
    map_entry = re.match("^[0-9 ]+$", line)

    if map_seeds:
        seeds = [int(seed) for seed in line.replace("seeds: ", "").split()]
    if map_start:
        map_type = map_start[1]
        maps[map_type] = []
    elif map_entry:
        dest, src, length = map_entry[0].split()
        maps[map_type].append({ "src": int(src), "dest": int(dest), "length": int(length) })

results = []

for seed in seeds:
    for m in maps.values():
        seed = get_next(seed, m)
    results.append(seed)

print(min(results))