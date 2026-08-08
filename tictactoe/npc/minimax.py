import sys
import os
import math
from game_functions.is_available import is_available
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_functions.is_winner import check_winner

score_games:dict[bool|int:int] = {
    'O': 1,
    'X': -1,
    'tie': 0
}

def minimax(board:list[str], depth: int, is_maximizing) -> int:
    '''Minimax algorithm to return score'''
    winner = check_winner(board)
    if winner != False:
        return score_games[winner]

    if is_maximizing: #Check if its the NPC turn
        best_score = "-inf"
        for i in range(len(board)): #check space in the board
            if is_available(board, i): #check if selected spot is available
                board[i] = 'O'
                score:int = minimax(board, depth + 1, False)
                board[i] = ""
                best_score:int = max(score, best_score) #check score returned by minimax if greater then best_score takes value
        return best_score
    
    else: #Check human possible next turn
        best_score = "inf"
        for i in range(len(board)): #check space in the board
            if is_available(board, i): #check if selected spot is available
                board[i] = 'X'
                score:int = minimax(board, depth + 1, True)
                board[i] = ""
                best_score:int = min(score, best_score) #check score returned by minimax if greater then best_score takes value
        return best_score