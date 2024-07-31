with open("./4/input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

total = 0
for line in lines:
	line = line[line.find(':')+1:].strip()
	winners, nums = line.split('|')
	nums = set([int(n) for n in nums.split()])
	winners = set([int(n) for n in winners.split()])
	win_count = len(nums.intersection(winners))
	
	if win_count > 0:
		points = 2**(max(win_count-1, 0))
		total += points
	else:
		continue

print(total)