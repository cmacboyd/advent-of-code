with open("./6/input.txt", "r") as f:
	lines = f.readlines()

import re
from math import prod
times = [int(t.strip()) for t in re.findall('\s\d+', lines[0])]
distances = [int(d.strip()) for d in re.findall('\s\d+', lines[1])]

record_breaks = []
for race_length, record in zip(times, distances):
	wins = 0
	for i in range(1, race_length):
		distance = i*(race_length-i)
		if distance > record:
			wins += 1

	record_breaks.append(wins)

print(record_breaks)
print(prod(record_breaks))

