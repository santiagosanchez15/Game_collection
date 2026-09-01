from userObject import User

def blackjack(user: User, house: House): #pseudocode for balckjack game
    '''BlackJack game
    True -> User wins
    False -> The House wins | tied

    '''

    #Get initial Draw for the user
    user.Intial_Draw()
    house.Initial_Draw()

    if user.is_over21() is True:
        print("The house wins, you lost!")
        return False
    if house.is_over21() is True:
        print("You won! Congratulations!!")
        return True

    while True: 

        #check if any of the players wants another card
        user.get_Card()
        house.get_Card()

         #Check if None of the players wants to keep playing
        if user.wantsCard is False and house.wantsCard is False:
            return user.check_winner(house)

        #FIXME need a function to recalcualte all the ace in the deck Maybe a dict that has a count of the number of card like {"A": 1, "2": 0, } value given by that
        

        #Check if any of the players is 21
        if user.is_over21():
            print(f"The house wins, you lost, you are over 21, the house got {house.Get_total()}!")
            return False

        if house.is_over21():
            print(f"You won the House is over 21! Congratulations!!")
            return True

       


