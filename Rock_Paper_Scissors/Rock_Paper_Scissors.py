from results_dict import results

def game(user1_choice:str, npc_choice:str) -> bool:
    '''Checks options, returns winner| True-> User Wins| False->NPC wins, -1 for draw'''

    user_outcome:str = results[user1_choice][npc_choice]#get result

    if user_outcome == "win": #Player wins
        print("You WIN!!! ")
        return True
    elif user_outcome == "lose":# player loses
        print("NPC WINS and You LOSE!!!")
        return False

    print("There is a DRAW")
    return -1 #Draw

