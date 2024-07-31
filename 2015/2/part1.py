with open("./2015/2/input.txt", "r") as f:
	dimensions = [[int(x) for x in line.strip("\n").split('x')] for line in f.readlines()]

def get_paper_needed(dims):
    l, w, h = dims

    sa = 2*l*w + 2*w*h + 2*h*l
    extra = min([l*w, w*h, h*l])

    return sa + extra

total = 0
for dim in dimensions:
    total += get_paper_needed(dim)

print(total)
