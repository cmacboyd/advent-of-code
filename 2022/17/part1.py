from itertools import cycle, product

with open("./17/input.txt", "r") as f:
	jets = f.read()

jet = cycle(jets)
block = cycle(['-', '+', 'L', 'I', '8'])


# The tall, vertical chamber is exactly seven units wide. 
# Each rock appears so that its left edge is two units away from the left wall and 
# its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

def get_starting_position(hy, block):
	# hy = max(populated, key=lambda x: x[1])[1]

	if block == '-':
		return [[i, hy+4] for i in range(3,7)]
	elif block == '+':
		return [[4, hy+6],
		[3, hy+5], [4, hy+5], [5, hy+5],
				[4, hy+4]]
	elif block == 'L':
		return [
								  [5, hy+6],
								  [5, hy+5],
			[3, hy+4], [4, hy+4], [5, hy+4]
		]
	elif block == 'I':
		return [
			[3, hy+7],
			[3, hy+6],
			[3, hy+5],
			[3, hy+4]
		]
	elif block == '8':
		return [
			[3, hy+5], [4, hy+5],
			[3, hy+4], [4, hy+4]
		]


def move_allowed(populated, position):
	# check for existing rocks
	if any([tuple(coords) in populated for coords in position]):
		return False

	# check for a wall
	elif any([x <= 0 or x >=8 for x,_ in position]):
		return False

	else:
		return True

counter = 0
populated = set([(i, 0) for i in range(9)])
highest_y = 0
while counter < 2023:
	# if counter % 100 == 0 or counter == 2022:
	print(f"Placing rock {counter}")
	
	# introduce block
	this_block = next(block)
	position = get_starting_position(highest_y, this_block)

	# do the moves starting with a jet
	move = cycle(['jet', 'down'])
	while True:
		move_type = next(move)
		if move_type == 'jet':
			# get the direction of the jet
			this_jet = next(jet)

			if this_jet == '<':
				# try to move left
				try_position = [[x-1, y] for x,y in position]
			elif this_jet == '>':
				# try to move right
				try_position = [[x+1, y] for x,y in position]

		elif move_type == 'down':
			# try to move down
			try_position = [[x, y-1] for x,y in position]


		allowed = move_allowed(populated, try_position)
		if allowed:
			# allowed move, set the position to the attempted position
			position = try_position
		elif not allowed and move_type == 'down':
			# rock is at rest, add it to populated, increment counter and break
			populated = populated.union(set([tuple(p) for p in position]))
			highest_y = max(highest_y, max(position, key=lambda x: x[1])[1])
			counter += 1
			break
		elif not allowed and move_type == 'jet':
			# the position we are trying is not allowed via jet, so just continue to try next move
			continue


# printing output to compare to example
# grid = [['.' for i in range(1,8)] for j in range(1,25)]
# print('\n'.join([''.join(row) for row in grid[::-1]]))

# for x,y in product(range(1,8), range(1,25)):
# 	if [x,y] in populated[9:]:
# 		print(x,y)
# 		grid[y-1][x-1] = '#'

# print('\n'.join([''.join(row) for row in grid[::-1]]))

highest_point = max(populated, key=lambda x: x[1])
print(highest_point[1]-2)


