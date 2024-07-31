import re
from collections import defaultdict
from math import inf

with open("./2015/9/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# build the graph
graph = defaultdict(dict)
for line in lines:
    src, dst, dist = re.match(r"([A-Za-z]+) to ([a-zA-Z]+) = (\d+)", line).groups()
    graph[src][dst] = int(dist)
    graph[dst][src] = int(dist)

node_count = len(graph)

def dfs(path):
    possible_nodes = {k: v for k,v in graph[path[-1][0]].items() if k not in [p[0] for p in path]}
    if not possible_nodes and len(path) < node_count:
        return -inf # this path won't visit all nodes
    elif not possible_nodes and len(path) == node_count:
        return sum([p[1] for p in path])

    return max([dfs(path+[(node, dist)]) for node, dist in possible_nodes.items()])

# Try starting at each node of the graph
max_path = -inf
for node in graph.keys():
    max_path = max(dfs([(node, 0)]), max_path)

# create a set of visited nodes
print(max_path)
