with open("./6/input.txt", "r") as f:
	lines = f.readlines()

import re
from math import prod
times = [t.strip() for t in re.findall('\s\d+', lines[0])]
distances = [d.strip() for d in re.findall('\s\d+', lines[1])]

time = int(''.join(times))
record = int(''.join(distances))

# probably some way to optimize this but yolo
wins = 0
for i in range(1, time):
	distance = i*(time-i)
	if distance > record:
		wins += 1

print(wins)

