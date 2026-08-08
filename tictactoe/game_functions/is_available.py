
def is_available(array_game:list[str], space:int)->bool:
    '''Returns True if place is empty if not then False'''
    return array_game[space] == " "