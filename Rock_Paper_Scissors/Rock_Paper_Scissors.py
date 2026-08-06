from results_dict import results

def main(user1_choice:str, npc_choice:str) -> bool:
    '''Checks options, returns winner| True-> User Wins| False->NPC wins, -1 for draw'''

    user_outcome:str = results[user1_choice][npc_choice]
    if user_outcome == "win":
        return True
    elif user_outcome == "lose":
        return False
    return -1

