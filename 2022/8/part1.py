from itertools import product

with open("./8/input.txt", "r") as f:
	lines = f.readlines()

trees = [[int(s) for s in line.strip()] for line in lines]

def is_visible(i, j):
	this_tree = trees[i][j]
	# Note I realize these directions are wrong in part2, kept them here
	from_top = all([trees[i][k] < this_tree for k in range(j-1, -1, -1)])
	from_bottom = all([trees[i][k] < this_tree for k in range(j+1, len(trees))])
	from_left = all([trees[h][j] < this_tree for h in range(i-1, -1, -1)])
	from_right = all([trees[h][j] < this_tree for h in range(i+1, len(trees[0]))])
	if from_top or from_bottom or from_right or from_left:
		return True
	else:
		return False

visible_trees = 0
for i, j in product(range(len(trees[0])), range(len(trees))):
	if is_visible(i, j):
		visible_trees += 1

print(f"There are {visible_trees} visible trees")
