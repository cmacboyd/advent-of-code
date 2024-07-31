import re
from math import inf
import heapq
from functools import cache
from itertools import product

with open("./16/input.txt", "r") as f:
	lines = f.readlines()

# Setup from input
pattern = r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnel lead to valve ([^$\n]+)"

valves = {}
for line in lines:
	line = line.replace("valves", "valve").replace("tunnels", "tunnel").replace("leads", "lead")
	if (match:=re.match(pattern, line)):
		valve_name, flow_rate, lead_to = match.groups()
		valves[valve_name] = {"flow": int(flow_rate), "leads_to": [v.strip() for v in lead_to.split(",")]}
	else:
		raise ValueError("Bad Regex")


# Setup a simplified graph using djikstra's algorithm
graph = {v: valves[v].get('leads_to') for v in valves.keys()}

# for a given src, destination, and graph, compute the shortest path from src -> dst
def get_shortest_path(src, dst, graph):
	distances = {node: inf for node in graph.keys()}
	distances[src] = 0 # start at the source node
	min_dist = [(0, src)]
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
		
	# sanity check
	if len(visited) != len(distances): 
		print("eeeeeek")

	# get the distance to the ending position
	return distances.get(dst)

nonzero_valves = [v for v in valves.keys() if valves[v].get('flow') != 0] + ['AA'] # Add AA because we start there
distances = {valve: {dst: get_shortest_path(valve, dst, graph) for dst in nonzero_valves if dst != valve} for valve in nonzero_valves}

# Core solution, now the nasty part
# Perform graph traversal while tracking time and pressure released

# computation of potential total pressure released if travelled to valve and released it
def get_potential(t, d, v):
	# potential pressure left is time remaining after travelled and release times flow rate
	return (t-d-1)*valves[v].get('flow')


# caching for speedup if we compute a path we have already seen
@cache
def dfs(t, person_free, elephant_free, person_path, elephant_path, released, pressure):
	if t <= 0:
		return t, person_free, elephant_free, person_path, elephant_path, released, pressure

	if person_free == t:
		person_position = person_path[-2:]
		person_possibilities = {v: d for v, d in distances[person_position].items() if v not in released and d+1 < t}
		person_potentials = sorted([(v, get_potential(t, d, v)) for v, d in person_possibilities.items()], key=lambda x: x[1], reverse=True)
	else:
		person_potentials = None

	if elephant_free == t:
		elephant_position = elephant_path[-2:]
		elephant_possibilities = {v: d for v, d in distances[elephant_position].items() if v not in released and d+1 < t}
		elephant_potentials = sorted([(v, get_potential(t, d, v)) for v, d in elephant_possibilities.items()], key=lambda x: x[1], reverse=True)
	else:
		elephant_potentials = None
	

	# if the person and the elephant are busy do dfs with t -= 1
	if person_free != t and elephant_free != t:
		# we can't take any actions, we are just waiting a minute while person and elephant travel or open a valve
		return dfs(t-1, person_free, elephant_free, person_path, elephant_path, released, pressure)
	
	# if there are no possibilities left, return the state information
	if not elephant_potentials and not person_potentials:
		return t, person_free, elephant_free, person_path, elephant_path, released, pressure
	

	# perform a dfs for if we released each valve
	if person_potentials and elephant_potentials and (combined_potentials:=[(x,y) for x,y in product(person_potentials, elephant_potentials) if x[0] != y[0]]):
		# both the person and the elephant are free and can go somehwere to release a valve
		# if we don't have a combined potential
		return max(
			[
				dfs(
					t-1, 
					t-person_possibilities[pv]-1, # when the person is free again
					t-elephant_possibilities[ev]-1, # when the elephant is free again
					f'{person_path},{pv}', # the person's updated path when they are free
					f'{elephant_path},{ev}', # elephant updated path when free
					f'{released},{pv},{ev}', 
					pressure+epr+ppr
					) 
					for (pv, ppr), (ev, epr) in combined_potentials
			], key=lambda x: x[-1])
	elif person_potentials and elephant_potentials and not combined_potentials:
		# one valve left, choose the one with highest potential, idk if we get here
		# just assign it to the person lol
		person_potentials = max(person_potentials, elephant_potentials, key=lambda x: x[0][1])


	if person_potentials:
		# dfs for person
		return max(
			[
				dfs(
					t-1, 
					t-person_possibilities[pv]-1, # when the person is free again
					elephant_free, # when the elephant is free again
					f'{person_path},{pv}', # the person's updated path when they are free
					elephant_path, 
					f'{released},{pv}', 
					pressure+ppr
					) 
					for pv, ppr in person_potentials
			], key=lambda x: x[-1])
	elif elephant_potentials:
		# dfs for person
		return max(
			[
				dfs(
					t-1, 
					person_free, # when the person is free again
					t-elephant_possibilities[ev]-1, # when the elephant is free again
					person_path, # the person's updated path when they are free
					f'{elephant_path},{ev}', 
					f'{released},{ev}',
					pressure+epr
					) 
					for ev, epr in elephant_potentials
			], key=lambda x: x[-1])


print("Trying dfs, lord have mercy")
import time
start = time.time()
result = dfs(26, 26, 26, 'AA', 'AA', 'AA', 0)
end = time.time()

print(f"The best result is having a pressure release of {result[-1]}, took {end-start:02f} seconds")
print(result)
