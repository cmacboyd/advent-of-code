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
    position[ax] = sign[facing]*amount + position[ax]

print(f"Final position is {position}, or {sum(position)} blocks away")
