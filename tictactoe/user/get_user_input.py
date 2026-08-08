import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game_functions.is_available import is_available

def get_game_user_input()->int:
    '''Get user input'''

    user_input:str = input("Choose where to play between 0-8: ")
    if is_valid_game_option(user_input, "8") is False:
        return get_game_user_input()
    
    return int(user_input)
    

def is_valid_game_option(input:str, range:str) -> bool:
    '''Return True if option inside range otherwise False'''

    if len(input)> 1: 
        print("More than one number please try again\n")
        return False

    if input >="0" and input <= range:
        return True

    print("Invalild Input or Input out of range please try again... \n")
    return False

def get_game_difficutly()->int:
    '''returns NPC difficulty'''
    print("Please choose a difficulty between 0-2\n-0: easy\n-1: medium\n-2: hard")
    user_input:str = input("Choose a difficulty: ")
    if is_valid_game_option(user_input, "2") is False: #ask again wrong input
        return get_game_difficutly()

    return int(user_input)

def user_choice(board:list[str]) -> None:
    '''Check if space available if not, asks again, if available modifies game array'''

    user_option = get_game_user_input() #Get user Input
    if is_available(board, user_option): #Check if spot is available
        board[user_option] = "X" #Place players choice
        return
    else:
        print("No valid space, Please choose a different space to play\n")
        return user_choice(board) #Call again, space no available, recurisve call again until right spot is chosen
