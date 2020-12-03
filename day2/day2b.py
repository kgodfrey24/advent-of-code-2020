from collections import Counter

def character_exists_at_position_in_string(check_value, position, string):
    return string[position - 1] == check_value


f = open("day2\input.txt")
lines = f.readlines()

i = 0

for line in lines:
    split_line = line.split()
    check_value = split_line[1][0]
    split_range = split_line[0].split("-")

    position1 = int(split_range[0])
    position2 = int(split_range[1])
    position1_match = character_exists_at_position_in_string(check_value, position1, split_line[2])
    position2_match = character_exists_at_position_in_string(check_value, position2, split_line[2])

    if position1_match + position2_match == 1:
        i += 1

print(i)