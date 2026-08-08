import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_functions.is_available import is_available

def easy_choice(array_game:list[str]):
    '''in a loop choices next empty space'''
    for i in range(len(array_game)):
        if is_available(array_game=array_game, space=i):
            array_game[i] = 'O'
            break
    return 