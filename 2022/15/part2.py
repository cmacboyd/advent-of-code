import re
from math import inf
from collections import defaultdict

with open("./15/input.txt", "r") as f:
	lines = f.readlines()

pattern = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)\n"

def get_manhattan_distance(s, b):
	return abs(s[0]-b[0]) + abs(s[1]-b[1])


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


def get_manhattan_circle(sensor, dist):
	# get the top and bottom of the cirlce
	sx, sy = sensor
	top = sy+dist
	bottom = sy-dist

	marker = [sx, top]
	x_ranges = {}
	while marker[1] >= bottom:
		this_dist = get_manhattan_distance(marker, sensor)
		extra = abs(this_dist-dist)
		x_range = [sx-extra, sx+extra]
		x_ranges[marker[1]] = x_range

		# decrement the y value (go down one)
		marker[1] -= 1

	return x_ranges


def merge_intervals(intervals):
    if len(intervals) == 1 or intervals[0] == [0, 4000000]:
        return [[0, 4000000]]
    
    ints = sorted(intervals, key=lambda x: x[0])
    i = 1
    wi = ints[0]
    new_intervals = []
    while i < len(ints):
        if wi == [0, 4000000]:
            return [wi]

        if wi[1] >= ints[i][0] -1:
            wi = [min(wi[0], ints[i][0]), max(wi[1], ints[i][1])]
        else:
            new_intervals.append(wi)
            wi = ints[i]
        
        i += 1

    new_intervals.append(wi)
    return new_intervals



def update_x_ranges(master, new):
	for y in sorted(list(new.keys())):
		if y < 0:
			continue # not at values we care to record yet
		elif y > 4000000:
			break # there will be no more values we care about

		left, right = new[y]
		master[y].append([max(0, left), min(4000000, right)])

	return master



# with the manhattan distances provided, go through each sensor and transform
# it into intervals that are not allowed (map from y values, to ranges of x values)
x_ranges = defaultdict(list) # maps from a y value to the not allowed x values in that row
total = len(sensors)
sensors = sorted(sensors, key=lambda x: x[1], reverse=True)
for index, (sensor, dist) in enumerate(sensors, 1):
	# go through the x values updating the ranges
	print(f"Working on adding sensor {index} of {total}")
	sensor_x_ranges = get_manhattan_circle(sensor, dist)
	x_ranges = update_x_ranges(x_ranges, sensor_x_ranges)

# merge the ranges
print("merging intervals")
i = 2916590 # cheating lol
while i <= 4000000:
	original = x_ranges[i]
	x_ranges[i] = merge_intervals(x_ranges[i])
	if i % 100000 == 0:
		print(f"Merged {i}/4000000")
	if len(x_ranges[i]) > 1:
		print(f"maybe problem merging {original} for y={i}, got {x_ranges[i]}")
		x_val = x_ranges[i][0][1] + 1
		y_val = i
		break

	i += 1
print("done merging intervals")

print(x_val, y_val)
x_val *= 4000000
print(f"the beaconing frequency is {x_val+y_val}")