from copy import copy
from math import sqrt
from typing import List

with open("./9/input.txt", "r") as f:
	moves = [line.strip().split(" ") for line in f.readlines()]

# If the head is ever two steps directly up, down, left, or right from the tail, 
# the tail must also move one step in that direction so it remains close enough

# setup rope positions - the rope represents coordinates of H, 1, ..., 9
rope = [[0,0] for i in range(10)]
tail_positions = set()

# map a directional letter to x or y, and a positive or negative value
def move_head(head, direction: str, amount: int):
	sign = {
		'R': 1,
		'L': -1,
		'U': 1,
		'D': -1
	}

	if direction == 'R' or direction == 'L':
		for i in range(amount):
			head[0] += sign.get(direction)
			yield head
	else:
		for i in range(amount):
			head[1] += sign.get(direction)
			yield head

	# return head

def supremum_distance(p1: List[int], p2: List[int]):
	return max([abs(p1[i]-p2[i]) for i in range(len(p1))])

def move_helper(source, target):
	if target > source:
		return source + 1
	else:
		return source - 1


def move_tail(head, tail):
	if supremum_distance(head, tail) <= 1:
		# we don't move the tail
		return tail
	else:
		# we need to move the tail so that it's in a good spot
		# there are three cases to handle:

		# Case 1, same x value, different y value (move vertically)
		if head[0] == tail[0] and head[1] != tail[1]:
			tail[1] = move_helper(tail[1], head[1])

		# Case 2, same y value, different x value (move horizontally)
		elif head[0] != tail[0] and head[1] == tail[1]:
			tail[0] = move_helper(tail[0], head[0])

		# Case 3, different x value, different y value (move diagonally; i.e. vertical and horizontal)
		elif head[0] != tail[0] and head[1] != tail[1]:
			tail[0] = move_helper(tail[0], head[0])
			tail[1] = move_helper(tail[1], head[1])

		else:
			print("eeeek")
	
	return tail


# for each set of directions:
# - move the head of the rope
# - move the next link of the rope as if it was a tail following the previous link

# how does that look for the rest of the rope?
# - move head, return list of moves
# - move next link as tail using each intermediate step from the head as a guide


for direction, amount in moves:
	# move the head, recording the moves
	for step in move_head(rope[0], direction, int(amount)):
		rope[0] = step
		link = 1
		while link < len(rope):
			# process the link
			rope[link] = move_tail(rope[link-1], rope[link])

			if link == 9:
				tail_positions.add(str(rope[link]))

			# increment the link number
			link += 1
		

print(f"The tail was in {len(tail_positions)} positions")