from itertools import product

with open("./8/input.txt", "r") as f:
	lines = f.readlines()

trees = [[int(s) for s in line.strip()] for line in lines]
# scenic_scores = [[0 for i in range(len(trees[0]))] for j in range(len(trees))]

def get_direction_score(direction_walk):
	#print(direction_walk)
	if len(direction_walk) == 0:
		return 0

	# count starts at 1 if there is a tree there
	score = 0
	for dw in direction_walk:
		if dw:
			score += 1
		else:
			score += 1
			break
	return score

def get_scenic_score(i, j):
	this_tree = trees[i][j]
	#print(f"testing {i, j, this_tree}")
	left_score = get_direction_score([trees[i][k] < this_tree for k in range(j-1, -1, -1)])
	right_score = get_direction_score([trees[i][k] < this_tree for k in range(j+1, len(trees))])
	up_score = get_direction_score([trees[h][j] < this_tree for h in range(i-1, -1, -1)])
	down_score = get_direction_score([trees[h][j] < this_tree for h in range(i+1, len(trees[0]))])
	score = up_score * down_score * left_score * right_score
	#print(f"{this_tree, i, j}: score is {score} - {up_score, left_score, right_score, down_score}")
	return score


best_scenic_score = 0
for i, j in product(range(len(trees[0])), range(len(trees))):
	best_scenic_score = max(get_scenic_score(i,j), best_scenic_score)

print(f"The best scenic score is {best_scenic_score}")
