from math import inf

with open("input.txt", "r") as f:
    lines = f.readlines()

numbers = [int(line.strip()) for line in lines]
last_number = inf
increasing = 0

for number in numbers:
    if number > last_number:
        increasing += 1
    last_number = number

print(increasing)

