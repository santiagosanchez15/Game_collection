from easy_difficulty import easy_choice
from medium_difficulty import medium_choice
from hard_difficulty import Best_Next_Move

def npc_choice(board:list[str], difficulty:int):
    '''Takes array, takes difficulty choosen, then selects and places next move'''

    if difficulty == 0:
        easy_choice(board) #next available space
        return
    if difficulty == 1:
        medium_choice(board) #next random space
        return 
    Best_Next_Move(board) #minimax i hope you work please
    return