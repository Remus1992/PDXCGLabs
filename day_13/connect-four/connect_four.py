grid_01 = [0, 0, 0, 0, 0, 0, 0] # bottom row
grid_02 = [0, 0, 0, 0, 0, 0, 0]
grid_03 = [0, 0, 0, 0, 0, 0, 0]
grid_04 = [0, 0, 0, 0, 0, 0, 0]
grid_05 = [0, 0, 0, 0, 0, 0, 0]
grid_06 = [0, 0, 0, 0, 0, 0, 0]
grid_07 = [0, 0, 0, 0, 0, 0, 0]

grids = [grid_07, grid_06, grid_05, grid_04, grid_03, grid_02, grid_01]

def grid_def():
    print ("",grid_01,"\n",grid_02,"\n",grid_03,"\n",grid_04,"\n",grid_05,"\n",grid_06,"\n",grid_07,"\n")

# grid_def()

player_01_turns = {}
player_02_turns = {}

with open('connect-four-moves.txt', 'r') as file:
    moves = file.read().split('\n')

    for index in range(len(moves)):
        # print (moves)
        if index %2 == 0:
            player_01_turns[index + 1] = moves[index]
            # Player 1:  {1: '4', 3: '5', 5: '4', 7: '5', 9: '6', 11: '7', 13: '3', 15: '4', 17: '6', 19: ''}
        else:
            player_02_turns[index + 1] = moves[index]
            # Player 2:  {2: '3', 4: '6', 6: '4', 8: '3', 10: '2', 12: '7', 14: '7', 16: '5', 18: '5'}

def placement_def(userInput, user):
    counter = 0
    for i in range (0,7):
        if (grids[i][userInput - 1] == 0):
            grids[i][userInput - 1] = int(user)
            grid_def()
            break

# print ("Player 1: ", player_01_turns)
# print ("Player 2: ", player_02_turns)

def play_game():
    for x in range(len(player_01_turns) + len(player_02_turns)):
        if x in player_01_turns:
            print ("Player 1 choses: ", player_01_turns [x])
            placement_def(int(player_01_turns [x]), 1)
        elif x in player_02_turns:
            print ("Player 2 choses: ", player_02_turns [x])
            placement_def(int(player_02_turns [x]), 2)

play_game()
