with open("./2015/1/input.txt", "r") as f:
	instructions = f.read()

floor = 0 
for index, char in enumerate(instructions, 1):
    if char == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        break

print(index)