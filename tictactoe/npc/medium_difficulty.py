import sys
import os
from random import randint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_functions.is_available import is_available

def medium_choice(array_game):
    '''NPC medium difficulty choice random choice'''
    counter:int = 0
    while(True):
        choice:int = randint(0,8)
        if is_available(array_game=array_game, space=choice ):
            array_game[choice] = "O"
            break
        if counter > 9:
            raise ValueError(-1)
        counter += 1
    return 
