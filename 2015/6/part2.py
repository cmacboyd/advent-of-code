import re

with open("./2015/6/input.txt", "r") as f:
	lines = [line.strip("\n") for line in f.readlines()]

pattern = r'(turn off|toggle|turn on) (\d+,\d+)( through )(\d+,\d+)'
grid = [[0 for i in range(1000)] for i in range(1000)]

print(len(grid), len(grid[0]))

for line in lines:
    instruction, start, _, end = re.match(pattern, line).groups()
    start = [int(i) for i in start.split(",")]
    end = [int(i) for i in end.split(",")]

    if instruction == 'turn on':
        # turn on the lights
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[y][x] += 1

    elif instruction == 'turn off':
        # turn off the lights
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[y][x] = max(grid[y][x]-1, 0)

    elif instruction == 'toggle':
        # toggle the lights
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                grid[y][x] += 2

    else:
        print("eeekk")


print(sum([sum(row) for row in grid]))