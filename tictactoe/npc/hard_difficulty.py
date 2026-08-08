import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_functions.is_available import is_available
from .minimax import minimax

def Best_Next_Move(array_game:list[str], depth, isMaximizingPlayer):
    '''Best move to be taken'''
    best_score = float('-inf')
    current_best_move = float('inf')
    
    for i in range(len(array_game)):#loop through the board

        if is_available(array_game,i): #check if available if so, add it
            array_game[i] = 'O' #give value to space taken

            score:int = minimax(array_game, 0, False) #get score from MiniMax algorithm
            array_game[i] = ' '#Give space previous value, no need to allocate more memory for another array

            if score > best_score: #check if score beats previous best score if so, update
                best_score = score
                current_best_move = i #update best move
    array_game[current_best_move] = 'O'

