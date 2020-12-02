f = open("day2\input.txt")
lines = f.readlines()
#print(lines)

sample = "4-5 r: rrrjr"

split_sample = sample.split()

print(split_sample)

print(split_sample[0])

split_range = split_sample[0].split("-")

print(split_range)

smallest = int(split_range[0])
largest = int(split_range[1])
print(f"smallest = {smallest} and largest = {largest}")

print(split_sample[1][0])