import random
def get_npc_input() -> str:
    '''Choses random option for npc input'''
    return random.choice(['rock', 'paper', 'scissors'])