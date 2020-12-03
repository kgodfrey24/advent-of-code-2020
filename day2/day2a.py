from collections import Counter

f = open("day2\input.txt")
lines = f.readlines()

i = 0

for line in lines:

    split_line = line.split()

    split_range = split_line[0].split("-")

    smallest = int(split_range[0])
    largest = int(split_range[1])

    check_value = split_line[1][0]

    count_totals = Counter(split_line[2])

    value_total = count_totals.get(check_value,0)



    print(f"{smallest} {largest} {check_value} {count_totals}")

    if value_total >= smallest and value_total <= largest:
        i += 1

print(i)

    
