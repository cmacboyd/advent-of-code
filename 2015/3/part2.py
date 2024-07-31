with open("./2015/3/input.txt", "r") as f:
	instructions = [i for i in f.read()]

robot_instructions = []
santa_instructions = []

i = 0
while i < len(instructions):
    if i % 2 == 0:
        santa_instructions.append(instructions[i])
    else:
        robot_instructions.append(instructions[i])

    i += 1

delivered = [str([0,0])]
for instructions in [robot_instructions, santa_instructions]:
    pos = [0, 0]
    for char in instructions:    
        if char == '<':
            pos[0] -= 1
        elif char == '>':
            pos[0] += 1
        elif char == '^':
            pos[1] += 1
        elif char == 'v':
            pos[1] -= 1
        else:
            print("eeek")

        delivered.append(str(pos))

print(len(set(delivered)))

