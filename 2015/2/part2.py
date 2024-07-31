from functools import reduce

with open("./2015/2/input.txt", "r") as f:
	dimensions = [[int(x) for x in line.strip("\n").split('x')] for line in f.readlines()]

def get_ribbon_needed(dims):
    smaller = [2*d for d in sorted(dims)[:2]]
    return sum(smaller) + reduce(lambda x,y: x*y, dims)

total = 0
for dim in dimensions:
    total += get_ribbon_needed(dim)

print(total)
