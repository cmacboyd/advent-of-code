import re

with open("./5/input.txt",  "r") as f:
    lines = [line for line in f.readlines()]

setup = lines[:lines.index('\n')][::-1]
instructions = lines[lines.index('\n')+1:]

stack_bottoms = setup.pop(0)
stack_numbers = re.findall(r"\d", stack_bottoms) # easy regex, there's just 9 in actual input
stacks = {number: [] for number in [int(sn) for sn in stack_numbers]}

# Build initial state
for s in setup:
    matches = re.search(r"^.(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.).$", s).groups()
    for stack, item in enumerate(matches, 1):
        if item == ' ':
            continue
        
        stacks[stack].append(item)

print(stacks)
# perform instructions
pattern = r"move (\d+) from (\d+) to (\d+)"
for instruction in instructions:
    match = re.match(pattern, instruction)
    amount, src, dest = [int(num) for num in match.groups()]

    while amount > 0:
        stacks[dest].append(stacks[src].pop())
        amount -= 1


print("".join([str(stacks[ind].pop()) for ind in range(1,10)]))
