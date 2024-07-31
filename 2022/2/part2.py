# Read in the file
with open("./2/input.txt", "r") as f:
    lines = (line.strip().split(" ") for line in f.readlines())

games = [line for line in lines]

opponent_mapper = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

outcome_mapper = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

choice_points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

winning_choice = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock'
}

# Reverse the winning chocie for losing choices
losing_choice = {v:k for k,v in winning_choice.items()}

game_point_mapper = {
    'Lose': 0,
    'Draw': 3,
    'Win': 6
}

def get_choice_points(decoded_opponent_choice, decoded_outcome):
    if decoded_outcome == 'Win':
        return choice_points.get(winning_choice.get(decoded_opponent_choice))
    elif decoded_outcome == 'Draw':
        return choice_points.get(decoded_opponent_choice)
    elif decoded_outcome == 'Lose':
        return choice_points.get(losing_choice.get(decoded_opponent_choice))


def get_all_points(opponent_choice, game_outcome):
    decoded_outcome = outcome_mapper.get(game_outcome)
    game_points = game_point_mapper.get(decoded_outcome)
    decoded_opponent_choice = opponent_mapper.get(opponent_choice)
    return game_points + get_choice_points(decoded_opponent_choice, decoded_outcome)

# Test scenario
# games = [
#     ['A', 'Y'],
#     ['B', 'X'],
#     ['C', 'Z']
# ]

total = sum([get_all_points(*game) for game in games])
print(f"The total is {total}")