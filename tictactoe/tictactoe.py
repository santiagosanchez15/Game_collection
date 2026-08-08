# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from user.get_user_input import get_game_difficutly, user_choice
from npc.get_npc_choice import npc_choice
from game_functions.is_winner import check_winner
from game_functions.print_board import print_board


def tictactoe() -> str:
    '''
    TicTacToe game
    X-> player wins
    O -> Player lose
    tie -> Draw
    '''
    #initialize values
    game_board:list[str|int] = [" "] * 9 #create array to play with
    game_difficulty:int = get_game_difficutly() # get diffuclty desire by player once set up it wont change


    while True: #inifite loop until someone wins

        #Machine will always start for now

        npc_choice(board=game_board, difficulty=game_difficulty) #NPC moves
        result = check_winner(game_board) #Check if someone won or tied
        print_board(game_board) #prints game board
        
        if result != False:
            return result
        
        user_choice(board=game_board)
        result = check_winner(game_board) #Check if someone won or tied
        print_board(game_board) # prints game board
        if result != False: #return value
            return result
    
