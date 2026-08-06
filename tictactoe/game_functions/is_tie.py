
def add_counter() ->bool:
    '''using currying will check if 
    needs to be given to variable and then varibale ()
    then counter increments
    '''
    counter:int = 0 

    def is_tie():
          nonlocal counter 
          counter += 1
          return counter == 9

    return is_tie