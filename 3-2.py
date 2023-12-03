import re
from functools import reduce
from common.cli import get_input

matrix = [list(l) for l in get_input()]

counter = 0

for i in range(0, len(matrix)):
    x, y = 0, 0
    for j in range(0, len(matrix[i])):
        char = matrix[i][j]

        if char == "*":
            x, y = i, j
            nums = []

            for x_transform in [-1, 0, 1]:
                if x_transform + x < 0 or x_transform + x >= len(matrix):
                    continue
                else:
                    row = x + x_transform

                dstr = ""

                for y_transform in [-1, 0, 1]:
                    k = y_transform
                    dchar = matrix[row][y + k]

                    if y_transform == -1:
                        while dchar.isdigit():
                            dstr = dchar + dstr
                            k -= 1
                            dchar = matrix[row][y + k]
                    
                    if y_transform == 0:
                        if dchar.isdigit():
                            dstr = dstr + dchar

                        elif dstr:
                            nums.append(dstr)
                            dstr = ""

                    if y_transform == 1:
                        while dchar.isdigit():
                            dstr = dstr + dchar
                            k += 1
                            if y + k >= len(matrix[row]):
                                break
                            dchar = matrix[row][y + k]

                if dstr:
                    nums.append(dstr)

            if len(nums) != 2:
                continue

            counter += reduce(lambda x, y: int(x) * int(y), nums)

print(counter)