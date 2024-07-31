import string
from functools import reduce
from itertools import cycle

with open("./3/input.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

elf_groups = [[]]
for line in lines:
    if len(elf_groups[-1]) < 3:
        elf_groups[-1].append(set(line))
    else:
        elf_groups.append([set(line)])

priorities = {letter: priority for priority, letter in enumerate(string.ascii_letters, 1)}
priority_sum = sum([priorities.get(reduce(lambda x, y: x.intersection(y), elf_group).pop()) for elf_group in elf_groups])

print(f"The sum of the priorities is {priority_sum}")