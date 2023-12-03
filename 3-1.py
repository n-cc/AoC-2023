import re
from common.cli import get_input

matrix = [list(l) for l in get_input()]

count = 0

for i in range(0, len(matrix)):
    num = ""
    x, y = 0, 0
    for j in range(0, len(matrix[i])):
        char = matrix[i][j]

        if char.isdigit():
            if not num:
                x, y = i, j
            num += char
        
        if num and (not char.isdigit() or len(matrix[i]) == j + 1):
            boundaries = []

            if not y == 0:
                boundaries.append(matrix[x][y - 1])
            if not y + len(num) + 1 > len(matrix[x]):
                boundaries.append(matrix[x][y + len(num)])

            for value in [-1, 1]:
                if value + x < 0 or value + x >= len(matrix):
                    continue
                else:
                    row = x + value

                if y == 0:
                    start = 0
                else:
                    start = y - 1

                if y + len(num) >= len(matrix[x]):
                    end = y + len(num)
                else:
                    end = y + len(num) + 1

                boundaries.append("".join(matrix[row][start:end]))

            for boundary in boundaries:
                if not re.match(r"^\.+$", boundary):
                    count += int(num)
                    break

            num = ""
            x, y = 0, 0

print(count)