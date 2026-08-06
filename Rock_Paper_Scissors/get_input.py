
def get_user_input()->str:
    '''Get User Input'''

    user_input:str = input("Choose only one option| Rock, Paper, Scissors: ")
    valid:bool = valid_choice(user_input)

    if valid is False: return get_user_input()
    return user_input



def valid_choice(choice:str)->bool:
    '''Returns true if valid choice, false if not'''

    choices = ['rock', 'paper', 'scissors']

    if choice.lower() in choices:
        return True

    print(f"{choice} is not valid, please try again...")
    return False