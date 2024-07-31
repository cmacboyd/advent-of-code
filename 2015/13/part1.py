import re
from collections import defaultdict
from itertools import permutations

with open("./2015/13/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

relationships = defaultdict(dict)

for line in lines:
    name1, rel, amount, name2 = re.match(r'([A-Za-z]+) would (lose|gain) (\d+) happiness units by sitting next to ([A-Za-z]+)', line).groups()

    sign = -1 if rel == 'lose' else 1

    relationships[name1][name2] = sign * int(amount)




names = relationships.keys()
optimal = (None, -99999)

def get_happiness(p):
    happiness = 0
    i = 0
    while i < len(p):
        if i == 0:
            left = p[-1]
        else:
            left = p[i-1]

        if i == len(p)-1:
            right = p[0]
        else:
            right = p[i+1]

        happiness += relationships[p[i]][left] + relationships[p[i]][right]
        i += 1

    return happiness

for p in permutations(names, 8):
    optimal = max((p, get_happiness(p)), optimal, key=lambda x: x[1])

print(optimal)