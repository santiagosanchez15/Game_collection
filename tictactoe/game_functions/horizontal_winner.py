
def horizontal_winner(array_game:list[str], player_symbol:str)->bool:
    '''Returns True if player wins or Flase if it doesn't'''

    if array_game[0] == player_symbol and array_game[1] == player_symbol and array_game[2] == player_symbol:
        return True
    elif array_game[3] == player_symbol and array_game[4] == player_symbol and array_game[5] == player_symbol:
        return True
    elif array_game[6] == player_symbol and array_game[7] == player_symbol and array_game[8] == player_symbol:
        return True

    return False 