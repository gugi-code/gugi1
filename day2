# importing the "guide" and splitting to different lines per round
with open("d2.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# dictionary for inputs : matching shape
input = {'A': 'Rock',
         'B': 'Paper',
         'C': 'Scissors',
         'X': 'Rock',
         'Y': 'Paper',
         'Z': 'Scissors'}
# dictionary for input : score we get
input_score = {'Rock': 1,
               'Paper': 2,
               'Scissors': 3}
# dictionary for win/loss/draw : score we get
outcome_score = {'Lose': 0,
                 'Draw': 3,
                 'Win': 6}
total_score = 0 # total score for later


def points_per_round(i):  # function to calculate points per round 
    opponent = input[i[0]] # opponents input is the one in position 1 of line
    us = input[i[2]] # our inputs in position 3 of line

    if opponent == us:
        return outcome_score['Draw'] + input_score[us] # if we tie, return 3 [key for draw] + our inputs score
    elif (opponent, us) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]: # possible loss outcomes
        return outcome_score['Lose'] + input_score[us] # if we lose, return 0 [key for lose] + our inputs score
    else: # if we aren't drawing or losing, we won
        return outcome_score['Win'] + input_score[us] # if we win, return 6 [key for win] + our inputs score

total_score = sum([points_per_round(i) for i in rounds])
print(total_score)
