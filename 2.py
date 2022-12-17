from common.fileOp import readFileLine

# We encode the choices with the numerical value this can be used to create a 2-d matrix for scoring and 
# additional scoring for choices

choice_mapping = {'A': 0, 'B': 1, 'C': 2,
                  'X': 0, 'Y': 1, 'Z': 2}

# we will map all the scenarios of rock paper scissors, victory is 6, draw 3 and loss is 0
score_matrix = [[3, 0, 6],
                [6, 3, 0],
                [0, 6, 3]]

# A 2-D representation for scenario where columns are opponents choice rock paper scissors and 
# Row is Loss, win and Draw the cell value gives the values of move for the give outcome and opponent move
                    #R #P #S
scenario_matrix =  [[2, 0, 1],  #Loss 
                    [0, 1, 2],  #Draw
                    [1, 2, 0]]  #Win

def calculate_score(opponent_choice, player_choice):
    opponent_index = choice_mapping[opponent_choice]
    player_index = choice_mapping[player_choice]

    player_score = player_index+1 + score_matrix[player_index][opponent_index]
    return player_score

def calculate_scenario_score(opponent_choice,scenario):
    # X: need to Loose 
    # Y: need to draw
    # Z: need to win
    opponent_index = choice_mapping[opponent_choice]
    scenario_index = choice_mapping[scenario]
    
    player_score = scenario_matrix[scenario_index][opponent_index]+1 + scenario_index*3 #+1 because I kept the points 0-indexed and win/loss/draw points
    return player_score

def runner(input):
    score = 0
    for match in input:
        opponent_choice , player_choice = match.split(' ')
        # score+=calculate_score(opponent_choice,player_choice)
        score+=calculate_scenario_score(opponent_choice,player_choice)
    return score

if __name__ == "__main__":
    input = readFileLine('2.txt')
    print(f" Final score for runner is {runner(input)}")
