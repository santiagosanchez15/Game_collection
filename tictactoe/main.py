from tictactoe import tictactoe
def main() -> bool:
    '''TicTacToe game to execute'''

    outcome = tictactoe()
    if outcome == 'X': #User Wins
        return True
    elif outcome == 'O': #User lose
        return False
    else: #There is a tie none wins
        return -1

print(main())