with open("./2/input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

import re
games = [(i, [g.split(',') for g in re.sub('Game \d+: ', '', l).split(';')]) for i, l in enumerate(lines, 1)]

requirements = {'red': 12, 'green': 13, 'blue': 14}
cube_regex = '(\d+) (blue|red|green)'
possible_games = []

for game_id, parts in games:
	maximums = {'red': 0, 'blue': 0, 'green': 0}
	possible = True

	# evaluate game
	# each part there are at most three draws of cubes
	for part in parts:
		part = [c.strip() for c in part]

		# looks at each number and colour draw of cube type
		for draw in part:
			amount, colour = re.match(cube_regex, draw).groups()
			maximums[colour] = max(maximums[colour], int(amount))
			if maximums[colour] > requirements[colour]:
				possible = False
				break

		if possible == False:
			break

	
	if possible == False:
		continue
	else:
		possible_games.append(game_id)

print(sum(possible_games))