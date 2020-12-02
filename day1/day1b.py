import sys

f = open("day1\input.txt")
lines = f.readlines()
values = list(map(int, lines))

target_value = 2020

for i in values:
    for j in values:
        for k in values:
            if i + j + k == 2020:
                print(f"{i} * {j} * {k} = {i*j*k}")
                sys.exit()