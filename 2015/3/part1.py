with open("./2015/3/input.txt", "r") as f:
	instructions = [i for i in f.read()]

pos = [0, 0]
delivered = [str([0,0])]
for i in instructions:
    if i == '<':
        pos[0] -= 1
    elif i == '>':
        pos[0] += 1
    elif i == '^':
        pos[1] += 1
    elif i == 'v':
        pos[1] -= 1
    else:
        print("eeek")


    delivered.append(str(pos))

print(len(set(delivered)))