with open("./5/test_input.txt", "r") as f:
	text = f.read()

import re
from collections import OrderedDict
from bisect import bisect

seeds = re.search('seeds:([\s\d]+)', text)
seeds = [int(n) for n in seeds.groups()[0].strip().split()]

# need to do some seed math here
roots = []
index = 0
while index < len(seeds):
	window = seeds[index:index+2]
	roots.append(window)
	index += 2

print(roots)
# print(sum([amount for start, amount in roots]))
# print(len(roots))


def get_map(name):
	match = re.search(f'{name} map:([\s\d]+)', text)
	lines = [[int(i) for i in line.split()] for line in match.groups()[0].strip().split('\n')]
	src_to_dst = OrderedDict()
	# TODO: you could sort the lines by src when making the map to help with faster lookups
	# then use ordered dictionary to do bisection search keys
	lines = [(src, dst, rng) for dst, src, rng in sorted(lines, key=lambda x: x[1])]
	for src, dst, rng in lines:
		src_to_dst.update({(src, src+rng-1): (dst, dst+rng-1)})
	return src_to_dst

maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
master_map = {
	k: v for k, v in [(m, get_map(m)) for m in maps]
}
print("done master map")
min_keys = {}
for name, mapping in master_map.items():
	print(f"assembling {name} min_keys")
	min_keys[name] = {rng[0]: rng for rng in mapping.keys()}
# min_keys = {name: {min(rng): rng for rng in mapping.keys()} for name, mapping in master_map.items()}
print("done min keys")


def get_outputs(input_rng, m='seed-to-soil'):
	print(f"\t{m}")
	ls, rs = input_rng
	# get the output ranges
	relevant_keys = [
		(start, stop) for (start, stop) in master_map[m].keys() 
		# interval intersects
		if (ls<=stop and ls>=start) or (rs<=stop and rs>=stop) or 
			# interval is strict subset
			(ls<=start and rs>=stop)
	]
	outputs = [master_map[m].get(rk) for rk in relevant_keys]

	# calc trim on keys and change to outputs
	if relevant_keys:
		trim_left = relevant_keys[0][0] - ls
		trim_right = rs - relevant_keys[-1][1]
		# if trim left is positive, add it to the output
		if trim_left > 0:
			outputs[0] = (outputs[0][0]+trim_left, outputs[0][1])
		if trim_right < 0:
			outputs[-1] = (outputs[-1][0], outputs[-1][1]+trim_right)

		# add the missing pieces to outputs if there are any
		i = 0 
		while i+1 < len(relevant_keys):
			print(f"compare ")
			# if there is a gap
			if relevant_keys[i][1]+1 < relevant_keys[i+1][0]:
				# fill it
				outputs.append((relevant_keys[i][1]+1, relevant_keys[i+1][0]-1))
			i += 1
		# check if we need to add to the end or start
		if relevant_keys[0][0] > ls:
			outputs.append((ls, relevant_keys[0][0]-1))
		if relevant_keys[-1][1] < rs:
			outputs.append((relevant_keys[-1][1]+1, rs))
	elif not relevant_keys and not outputs:
		outputs = [(ls, rs)]

	print(f"\trelevant keys: {relevant_keys}")
	print(f"\toutputs: {sorted(outputs, key=lambda x: x[0])}")
	
	return sorted(outputs, key=lambda x: x[0])

# maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
from numpy import Inf
min_loc = Inf
print(roots)
for index, (seed_start, seed_range) in enumerate(roots, 1):
	print(f"Processing seed range {index} of {len(roots)}")
	rng = (seed_start, seed_start+seed_range-1)
	locations = []
	print(rng)

	# I hate myself, this should be recursion
	soils = get_outputs(rng, 'seed-to-soil')
	print(f"soils, {soils}")
	for soil in soils:
		fertilizers = get_outputs(soil, 'soil-to-fertilizer')
		print(f"fertilizers {fertilizers}")
		for fertilizer in fertilizers:
			waters = get_outputs(fertilizer, 'fertilizer-to-water')
			for water in waters:
				lights = get_outputs(water, 'water-to-light')
				for light in lights:
					temperatures = get_outputs(light, 'light-to-temperature')
					for temperature in temperatures:
						humidities = get_outputs(temperature, 'temperature-to-humidity')
						for humidity in humidities:
							locs = get_outputs(humidity, 'humidity-to-location')
							locations.extend(locs)
	print(locations)

	min_loc = min(min_loc, min(locations, key=lambda x: x[0])[0])
print(min_loc)