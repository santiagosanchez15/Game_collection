from .diagonal_winner import diagonal_winner
from .vertical_winner import vertical_winner
from .horizontal_winner import horizontal_winner
from .is_tie import is_tie

def is_winner(array_game:list[str], player_symbol:str)->bool:
    '''returns if player wins'''
    return (
        diagonal_winner(array_game=array_game, player_symbol=player_symbol) or
        vertical_winner(array_game=array_game, player_symbol=player_symbol)or
        horizontal_winner(array_game=array_game, player_symbol=player_symbol)
    )

def check_winner(array_game) ->str:
    '''Returns winner state of game, varibale will adopt value of game state, therefore check variable if equal to one of those values then act'''
    #Check if user won
    if check_user_won(array_game):
        return 'X'

    #Check if NPC won
    if check_npc_won(array_game):
        return 'O'

    #Check if there is a tie
    if is_tie(array_game): # if true returns tie
        return 'tie'

    return False #no winner
   


def check_user_won(array_game:list[str])-> bool:
    '''Check if user Won'''

    return is_winner(array_game, 'X')

def check_npc_won(array_game:list[str]) -> bool:

    return is_winner(array_game, 'O')

    