from get_input import get_user_input
from npc_input import get_npc_input
from Rock_Paper_Scissors import game

def main():
    '''Actual Rock paper scissors game'''

    user_choice:str = get_user_input() #Get user input
    npc_choice:str = get_npc_input()#Get npc input
    return game(user1_choice=user_choice, npc_choice=npc_choice) #get result

  
