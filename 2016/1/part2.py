import sys

with open("./2016/1/input.txt", "r") as f:
	directions = [direction.strip() for direction in f.read().split(',')]


right_turn = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

left_turn = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}

sign = {
    'N': 1,
    'S': -1,
    'E': 1,
    'W': -1
}

axis = {
    'N': 0,
    'S': 0,
    'E': 1,
    'W': 1
}

position = [0, 0]
visited = set()
visited.add(tuple(position))

facing = 'N'
for direction in directions:
    turn = direction[0]
    amount = int(direction[1:])

    # turn to get new facing
    if turn == 'R':
        facing = right_turn[facing]
    elif turn == 'L':
        facing = left_turn[facing]
    
    # get axis of travl
    ax = axis[facing]

    # change position
    for i in range(amount):
        position[ax] = sign[facing] + position[ax]

        if tuple(position) in visited:
            print(f"First location to be visited twice is {position}, which is {sum([abs(p) for p in position])} blocks away")
            sys.exit()
        else:
            visited.add(tuple(position))

    # if tuple(position) in visited:
    #     break

print(position, sum(position))
