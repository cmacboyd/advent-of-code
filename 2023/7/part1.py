with open("./7/input.txt", "r") as f:
	lines = [l.split() for l in f.readlines()]

from collections import Counter
card_order = 'AKQJT98765432'
hand_order = [
	'Five of a kind',
	'Four of a kind',
	'Full house',
	'Three of a kind',
	'Two pair',
	'One pair',
	'High card'
]

def get_hand_type(hand):
	c = Counter(hand)
	if max(c.values()) == 5:
		return 'Five of a kind'
	elif max(c.values()) == 4:
		return 'Four of a kind'
	elif sorted(c.values()) == [2, 3]:
		return 'Full house'
	elif max(c.values()) == 3:
		return 'Three of a kind'
	elif sorted(c.values()) == [1, 2, 2]:
		return 'Two pair'
	elif max(c.values()) == 2:
		return 'One pair'
	else:
		return 'High card'

def ranking_score(hand):
	hand_score = (len(hand_order) - hand_order.index(get_hand_type(hand)))
	card_scores = [len(card_order) - card_order.index(c) for c in hand]
	return hand_score, *card_scores

outputs = []
for hand, bid in lines:
	ht = get_hand_type(hand)
	rs = ranking_score(hand)
	outputs.append((hand, rs, bid))

# sort based on ranking score tuple
outputs = sorted(outputs, key=lambda x: x[1])

s = 0
for rank, (hand, rs, bid) in enumerate(outputs, 1):
	s += rank*int(bid)

print(s)




