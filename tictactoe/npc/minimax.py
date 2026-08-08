import sys
import os
import math
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
    pass