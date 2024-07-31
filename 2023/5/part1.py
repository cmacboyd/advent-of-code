with open("./5/input.txt", "r") as f:
	text = f.read()

import re
seeds = re.search('seeds:([\s\d]+)', text)
seeds = [int(n) for n in seeds.groups()[0].strip().split()]

def get_map(name):
	match = re.search(f'{name} map:([\s\d]+)', text)
	lines = [[int(i) for i in line.split()] for line in match.groups()[0].strip().split('\n')]
	src_to_dst = {}
	# TODO: you could sort the lines by src when making the map to help with faster lookups
	# then use ordered dictionary to do bisection search keys
	for dst, src, rng in lines:
		src_to_dst.update({range(src, src+rng): range(dst, dst+rng)})
	return src_to_dst

maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
master_map = {
	k: v for k, v in [(m, get_map(m)) for m in maps]
}

def get_location(seed):
	result = seed
	for m in maps:
		print('\t', m)
		# TODO: instead of doing them all, you can be clever and bisection search start of intervals
		for rkey in master_map[m].keys():
			if result in rkey:
				# update the result
				dst = master_map[m].get(rkey)
				result = min(dst) + (result- min(rkey))
				break
			# otherwise the result stays the same and we go to the next map
	return result


from numpy import Inf
min_loc = Inf
for number, seed in enumerate(seeds, 1):
	print(f"processing seed #{number} of {len(seeds)}, {seed}")
	min_loc = min(min_loc, get_location(seed))

print(min_loc)

# answer 1181555926
# will optimize in part 2


# optimized part 2 below (ended up needing a different strategy using ranges)

# def get_map(name):
# 	match = re.search(f'{name} map:([\s\d]+)', text)
# 	lines = [[int(i) for i in line.split()] for line in match.groups()[0].strip().split('\n')]
# 	src_to_dst = OrderedDict()
# 	# TODO: you could sort the lines by src when making the map to help with faster lookups
# 	# then use ordered dictionary to do bisection search keys
# 	lines = [(src, dst, rng) for dst, src, rng in sorted(lines, key=lambda x: x[1])]
# 	for src, dst, rng in lines:
# 		src_to_dst.update({range(src, src+rng): range(dst, dst+rng)})
# 	return src_to_dst

# maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
# master_map = {
# 	k: v for k, v in [(m, get_map(m)) for m in maps]
# }
# print("done master map")
# min_keys = {}
# for name, mapping in master_map.items():
# 	print(f"assembling {name} min_keys")
# 	min_keys[name] = {rng.start: rng for rng in mapping.keys()}
# # min_keys = {name: {min(rng): rng for rng in mapping.keys()} for name, mapping in master_map.items()}
# print("done min keys")

# def get_result_from_map(m, rkey, result, master_map):
# 	dst = master_map[m].get(rkey)
# 	return dst.start + (result-rkey.start)

# def get_location(seed, master_map, min_keys):
# 	result = seed
# 	for m in maps:
# 		# print('\t', m)
# 		mks = list(min_keys[m].keys())

# 		# bisect right
# 		insertion_index = bisect(mks, result)

# 		# look at the range in the returned index (if available) and the range below (if available)
# 		if insertion_index > len(mks)-1:
# 			# we only need to look at the last entry
# 			if result in (rkey:=min_keys[m].get(mks[-1])):
# 				result = get_result_from_map(m, rkey, result, master_map)

# 		elif insertion_index == 0:
# 			# we only need to check the first entry
# 			if result in (rkey:=min_keys[m].get(mks[0])):
# 				result = get_result_from_map(m, rkey, result, master_map)

# 		else:
# 			# checking to the left and right
# 			if result in (rkey:=min_keys[m].get(mks[insertion_index])):
# 				result = get_result_from_map(m, rkey, result, master_map)

# 			if result in (rkey:=min_keys[m].get(mks[insertion_index-1])):
# 				result = get_result_from_map(m, rkey, result, master_map)

# 		# otherwise result is unchanged
# 	return result