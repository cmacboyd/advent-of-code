from string import ascii_lowercase
from math import inf
from itertools import product
from collections import defaultdict
import heapq


with open("./12/input.txt", "r") as f:
	lines = (line.strip() for line in f.readlines())

scores = {k: v for v, k in enumerate(ascii_lowercase, 1)}
scores['S'] = False
scores['E'] = 27

grid = [[scores.get(char) for char in row] for row in lines]
cols = len(grid[0])
rows = len(grid)

# find the starting ones:
start_positions = []
for i, j in product(range(rows), range(cols)):
	if grid[i][j] is False or grid[i][j] == 1:
		start_positions.append((i, j))
	if grid[i][j] == 27:
		end_position = (i, j)

# instantiate the graph
graph = defaultdict(dict)

# function for retrieving neighbours (building the graph)
def get_neighbours(node):
	i, j = node
	val = grid[i][j]
	
	potential_neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
	neighbours = []
	for y, x in potential_neighbours:
		# validity check
		if (y < 0 or x < 0 or y >= rows or x >= cols or grid[y][x] > val + 1 or grid[y][x] == False):
			continue
		else:
			neighbours.append((y, x))

	return neighbours

# build the graph
for node in product(range(rows), range(cols)):
	graph[node] = get_neighbours(node)

# djikstra's algorithm for the graph

# setup
distances = {node: inf for node in product(range(rows), range(cols))}
for sp in start_positions:
	distances[sp] = 0

min_dist = [(0, sp) for sp in start_positions]
visited = set() # visited nodes

# core algorithm
while min_dist:
	
	cur_dist, node = heapq.heappop(min_dist)
	if node in visited: # if this node has been visited, go to the next minimum distance
		continue
	visited.add(node)    
	
	for neighbor in graph[node]:
		if neighbor in visited: # if we have already visited the neighbour, move to the next neighbour
			continue

		# the distance to this node is the current distance travelled plus 1 (for unweighted vertices) 
		this_dist = cur_dist + 1 # graph[node][neighbor]

		# push onto the heap
		if this_dist < distances[neighbor]:
			distances[neighbor] = this_dist
			heapq.heappush(min_dist, (this_dist, neighbor))

# get the distance to the ending position
print(distances.get(end_position))
