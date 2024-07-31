import re
from math import inf

with open("./15/input.txt", "r") as f:
	lines = f.readlines()

pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)\n"

def get_manhattan_distance(s, b):
	return abs(s[0]-b[0]) + abs(s[1]-b[1])

max_dist = -inf
max_x = -inf
min_x = inf
max_y = -inf
min_y = inf
sensors = []
beacons = set()
for line in lines:
	if match:=re.match(pattern, line):
		xs, ys, xb, yb = [int(i) for i in match.groups()]
		sensor = (xs, ys)
		beacon = (xb, yb)
		beacons.add(beacon)
		dist = get_manhattan_distance(sensor, beacon)
		sensors.append((sensor, dist))
		max_dist = max(max_dist, dist)
		max_x = max([xs, max_x])
		min_x = min([xs, min_x])
		max_y = max([ys, max_y])
		min_y = min([ys, min_y])

# just a lil safety buffer
min_x -= max_dist
max_x += max_dist

target_row = 2000000

not_allowed_count = 0
for x in range(min_x, max_x+1):
	this_point = (x, target_row)
	if this_point in beacons:
		# skip checking, we know there is a beacon here
		continue

	for sensor, dist in sensors:
		if get_manhattan_distance(this_point, sensor) <= dist:
			not_allowed_count += 1
			break

print(not_allowed_count)
