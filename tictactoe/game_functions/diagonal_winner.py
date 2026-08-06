
def diagonal_winner(array_game:list[str], player_symbol:str)->bool:
    '''Returns True if player wins, false if didnt'''

    if array_game[0] == player_symbol and array_game[4] == player_symbol and array_game[8] == player_symbol:
        return True
    if array_game[2] == player_symbol and array_game[4] == player_symbol and array_game[6] == player_symbol:
        return True 
    return False