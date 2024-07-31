from math import inf
from itertools import product

with open("./14/input.txt", "r") as f:
	lines = [[tuple(eval(num) for num in i.split(",")) for i in item] for item in (line.strip("\n").split(" -> ") for line in f.readlines())]


MARGIN = 10000


# Grid setup
x_min = inf
x_max = -inf
y_min = inf
y_max = -inf
to_add = set()
for line in lines:
	i = 0
	
	while i+1 < len(line):
		# start point, finish point from line
		start, stop = line[i:i+2]
		start_x, start_y = start
		stop_x, stop_y = stop

		# update the grid size
		x_min = min([x_min, start_x, stop_x])
		x_max = max([x_max, start_x, stop_x])
		y_min = min([y_min, start_y, stop_y])
		y_max = max([y_max, start_y, stop_y])


		# populate the dots
		src, dst = sorted([start, stop])

		# 
		if src[0] == dst[0]:
			for x in range(src[1], dst[1]+1):
				to_add.add((src[0], x))

		elif src[1] == dst[1]:
			for y in range(src[0], dst[0]+1):
				to_add.add((y, src[1]))
		
		else:
			print("eeeek")

		i += 1


# sorting the rocks to add, to be civilized
to_add = sorted([(x[0]-x_min+MARGIN, x[1]) for x in to_add])
to_add.extend([(i, y_max+2) for i in range(-MARGIN, x_max+1-x_min+MARGIN)])

# draw the starting grid
cols = range(-MARGIN, x_max+1-x_min+MARGIN)
rows = range(0, y_max+3)
grid = [['.' for i in cols] for j in rows]
for i,j in to_add:
	grid[j][i] = '#'

# Utility function to see what we are doing
def print_grid(grid):
	print('\n'.join([' '.join([element for element in row]) for row in grid]))

# function to find the next spot for the sand to go, or return None if at rest
def next_spot(grid, i, j):
	# sanity check
	assert type(grid[i][j]) is str

	# check below (valid on grid)
	if i+1 < len(grid) and grid[i+1][j] == '.':
		# there is free space below, move down
		return i+1, j

	# check down-left (valid on grid)
	elif i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] == '.':
		# there is free space down and to the left, move there
		return i+1, j-1

	# check down-right (valid on grid)
	elif i+1 < len(grid) and j+1 < len(grid[0]) and grid[i+1][j+1] == '.':
		# there is free space down and to the right, move there
		return i+1, j+1

	# otherwise at rest or valid move off the board
	else:
		return None

# define how the sand is dropping
def drop_sand(grid, ssy, ssx):
	i = ssy
	j = ssx

	while next_spot(grid, i, j):
		i, j = next_spot(grid, i, j)

	# otherwise sand is at rest, update grid
	grid[i][j] = 'O'


# Start the sand falling!
ssy, ssx = (0, 500-x_min+MARGIN)

counter = 0
while grid[ssy][ssx] == '.':
	drop_sand(grid, ssy, ssx)
	counter += 1

print("\n\n=== final grid ===")
#print_grid(grid)
print(f"There were {counter} grains of sand falling before they fall into the abyss")