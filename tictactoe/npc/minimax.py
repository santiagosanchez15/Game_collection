import sys
import os
import math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_functions.is_winner import is_winner

score_games:dict[bool|int:int] = {
    True: 1,
    False: -1,
    -1: 0
}

def minimax(board:list[str], depth: int, is_maximizing) -> int:
    '''Minimax algorithm to return score'''
    if is_winner(board, 'O'):
        return 1
    pass