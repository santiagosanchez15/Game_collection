from diagonal_winner import diagonal_winner
from vertical_winner import vertical_winner
from horizontal_winner import horizontal_winner
import asyncio 

def is_winner(array_game:list[str], player_symbol:str)->bool:
    '''returns if player wins'''
    return (
        diagonal_winner(array_game=array_game, player_symbol=player_symbol), 
        vertical_winner(array_game=array_game, player_symbol=player_symbol),
        diagonal_winner(array_game=array_game, player_symbol=player_symbol)
    )