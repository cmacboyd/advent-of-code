with open("./4/input.txt", "r") as f:
	original_cards = [line.strip() for line in f.readlines()]

from functools import cache
card_to_wins = {}

# get original wins for lookup table
for card, line in enumerate(original_cards, 1):
	line = line[line.find(':')+1:].strip()
	winners, nums = line.split('|')
	nums = set([int(n) for n in nums.split()])
	winners = set([int(n) for n in winners.split()])
	win_count = len(nums.intersection(winners))
	card_to_wins[card] = win_count

# recursive function to calculate card wins
@cache
def get_card_wins(card):
	wins = card_to_wins.get(card)
	for i in range(card+1, card+wins+1):
		wins += get_card_wins(i)
	return wins

total_cards = len(original_cards)
card_count = total_cards
for card in range(1,total_cards+1):
	card_count += get_card_wins(card)

print(card_count)