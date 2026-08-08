
def is_tie(game_board:list[str]) ->bool:
    
    return all(cell != " " for cell in game_board)