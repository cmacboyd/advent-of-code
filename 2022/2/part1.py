# Read in the file
with open("./2/input.txt", "r") as f:
    lines = (line.strip().split(" ") for line in f.readlines())

games = [line for line in lines]

opponent_mapper = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

my_mapper = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

choice_points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

def game_win(doc, dmc):
    if dmc == 'Rock' and doc == 'Scissors':
        return True
    elif dmc == 'Scissors' and doc == 'Paper':
        return True
    elif dmc == 'Paper' and doc == 'Rock':
        return True
    else:
        return False

def get_choice_points(my_choice):
    return choice_points.get(my_mapper.get(my_choice))

def get_game_points(opponent_choice, my_choice):
    # Decoded opponent choice and decoded my choice
    doc = opponent_mapper.get(opponent_choice)
    dmc = my_mapper.get(my_choice)

    if doc == dmc:
        # Draw
        return 3
    elif game_win(doc, dmc):
        # Win
        return 6
    else:
        # Loss
        return 0 

def get_all_points(opponent_choice, my_choice):
    return get_choice_points(my_choice) + get_game_points(opponent_choice, my_choice)

# Test scenario
# games = [
#     ['A', 'Y'],
#     ['B', 'X'],
#     ['C', 'Z']
# ]

total = sum([get_all_points(*game) for game in games])
print(f"The total is {total}")