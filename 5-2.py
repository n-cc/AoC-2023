import re
from collections import OrderedDict
from common.cli import get_input

seeds = []
maps = OrderedDict()

map_type = ""

for line in get_input():
    map_seeds = re.match("^seeds:.*", line)
    map_start = re.match("^([A-Za-z-]+) map:$", line)
    map_entry = re.match("^[0-9 ]+$", line)

    if map_seeds:
        start = None
        for seed in [int(seed) for seed in line.replace("seeds: ", "").split()]:
            if not start:
                start = seed
            else:
                seeds.append({ "start": start, "length": seed })
                start = None

    if map_start:
        map_type = map_start[1]
        maps[map_type] = []
    elif map_entry:
        dest, src, length = map_entry[0].split()
        maps[map_type].append({ "start": int(src), "stop": int(src) + int(length), "transform": int(src) - int(dest) })

lowest = None

for entry in seeds:
    print(entry)
    for seed in range(entry["start"], entry["start"] + entry["length"]):
        for e in maps.values():
            for m in e:
                if m['start'] <= seed <= m['stop']:
                    seed = seed - m['transform']
                    break
        if not lowest or seed < lowest:
            lowest = seed

print(lowest)