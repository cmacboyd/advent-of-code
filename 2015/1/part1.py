with open("./2015/1/input.txt", "r") as f:
	instructions = (i for i in f.read())

floor = 0 
for i in instructions:
    if i == '(':
        floor += 1
    else:
        floor -= 1

print(floor)