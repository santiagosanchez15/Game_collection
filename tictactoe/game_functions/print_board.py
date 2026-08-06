
def print_board(array_game:list[str]):
    '''Prints boards game'''

    for i in range(len(array_game)):
        print(array_game[i] , end="")
        if i % 3 != 2:
            print("|",end="")
        else:
            print()
            if i != len(array_game) - 1:
                print("______")