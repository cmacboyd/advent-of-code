with open("./10/input.txt", "r") as f:
	instructions = [line.strip() for line in f.readlines()]

new_instructions = []
for instruction in instructions:
	if instruction == "noop":
		new_instructions.append(instruction)
	else:
		new_instructions.extend(["noop", instruction])


x = 1
special_cycles = [20, 60, 100, 140, 180, 220]
special_cycle_values = []

for cycle, instruction in enumerate(new_instructions, 1):
	if cycle in special_cycles:
		special_cycle_values.append(cycle*x)
	
	if instruction == "noop":
		pass
	else:
		addx, amount = instruction.split(' ')
		x += int(amount)

print(sum(special_cycle_values))
