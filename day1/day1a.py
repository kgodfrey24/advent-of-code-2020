f = open("day1\input.txt")
lines = f.readlines()
values = list(map(int, lines))

target_value = 2020

for i in values:
    counterpart = 2020-i
    if counterpart in values:
        print(f"{i} * {counterpart} = {i * counterpart}")
        break
    