from common.cli import get_input

def get_number(entry: str, mappings: dict) -> int:
    for i in range(0, len(entry)):
        if entry[i].isdigit():
            return entry[i]

        for match in mappings.keys():
            for j in range(0, len(match)):
                if entry[i + j] == match[j]:
                    continue
                else:
                    break
            else:
                return mappings[match]

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

counter = 0

for entry in get_input():
    first = get_number(entry, numbers)
    last = get_number(entry[::-1], { key[::-1]: value for key, value in numbers.items() })

    counter += int(f"{first}{last}")

print(counter)