import sys
import os
from random import choice
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playerObject import Player

class User(Player):
    '''User class inherits from Player'''

    def __init__(self, name : str |None):
        super().__init__(name=name)

    def Print_Cards(self):
        print("The cards in your deck are:\n")
        for card in self.deck:
            print(f"  -{card}")

    def Intial_Draw(self):
        '''Initial Draw for the User'''
        self.deck.append(choice(self.FullDeck)) #Get first Card
        self.deck.append(choice(self.FullDeck)) #Get Second Card
        self.Print_Cards()
        

    def Calculate_total_deck(self):
        '''Add value of card to the total of my deck'''
        self.ValueDeck = sum(self.ValueCards[card] for card in self.deck)  # sums all values of cards in deck #FIXME test that it works
        print(f'The new total value of your deck is {self.ValueDeck}')

    def Add_card_deck(self, card:str):
        '''Add given card to deck'''
        self.deck.append(card)
        self.Calculate_total_deck() #Recalculate total

    #Get Functions below

    def get_Card(self):
        '''Get a random card if input is yes'''

        print("Do you want another card?\n")
        self.wantsCard : bool = self.check_valid_yes_no() #ask if the user wants one more card 
        if self.wantsCard is False:
            return False #User didnt want another card
        
        card : str = choice(self.FullDeck) #Get a random card

        if self.Is_Ace(card): #Check if card is ace
            card = self.choose_value_ace() #Get value for Ace
        self.Add_card_deck(card) #add card to deck

    def check_valid_yes_no(self) -> bool:
        '''Check if input is valid yes or no'''

        user_input : str = input("yes or no only: ")
        clean_input = user_input.strip().lower() # clean input and lower the cases if upper cases
        
        try: #check if it falls in one of the cases otherwise call the function again
            if clean_input == "yes":
                return True
            if clean_input == "no":
                return False
    
            raise ValueError("Wrong input please try again\n")
    
        except ValueError as e: #Wrong input, call the function again
            print(e)
            return self.check_valid_yes_no()

    #Ace functions below

    def choose_value_ace(self) -> str:
        '''Player chose value ace'''
        print(f"You got and Ace! Your current total is: {self.ValueDeck}\n")
        user_input : str= self.is_valid_ace_value() #get user input
        return user_input #return value chosen

    def is_valid_ace_value(self) -> str:
        '''Check if input is valid ace value'''

        user_input : str= input("Do you want your card to be 1 or 11").lower().strip() #get clean input from user
        try: 
            if user_input != "1" or user_input != "11":
                raise ValueError
            return user_input

        except ValueError:
            print("Wrong input please try again| Only 1 or 11")
            return self.choose_value_ace()

    def Is_Ace(self, card:str) -> bool:
            '''Check if player got an ace, if so retrun true else no '''
            return card == "A"
    
    
    def num_ace_inDeck(self) -> int:
        '''Returns number of Ace in deck'''
        num_ace : int = self.deck.count("A") #Get num ace in deck
        print(f"You have {num_ace} Ace in your deck")
        return num_ace


    def Calculate_total_ace(self):
        '''Recalculate total depending on the number of Ace on deck'''

        print(f"The current value of your deck is f{self.ValueDeck}- Do you want to reacalculate your Ace value? ")
        wants_recalculate: bool = self.check_valid_yes_no()
        if wants_recalculate is False: #Didnt want to reacalculate return
            return
        num_ace_deck : int = self.num_ace_inDeck() #get number of ace in deck
        print(f"There are {num_ace_deck} Ace(s) in your deck\n")
        num_ace_recalculate : int = self.check_num_ace_recalcualte(num_ace_deck) #check the num of ace to recalculate
        num_changes :int = 0 # keep track of num changes

        #user choses new ace values
        for i, card in enumerate(self.deck): #loop through de cards

            if num_changes >= num_ace_recalculate: # change if num max of changes reached
                break

            if card != "11" or card != "1": #check if current card is an ace value
                continue

            print(f"The current card has a value of {card} do you want to change it?\n")
            wants_change :str = self.check_valid_yes_no()

            if wants_change is False: 
                continue
            
            self.deck[i] = self.choose_value_ace() #Choose new value for ace
            self.Calculate_total_deck() #Recalculate value
            num_changes += 1 #one more change

        return


    #FIXME maybe delete function below
    def check_num_ace_recalcualte(self, num_ace: int):
        '''Check valid input for number of ace to recalculate'''

        user_input : str= input("\nHow many ACE do you want to recalcualte? ").lower().strip() #get clean input from user
        try: 
            if user_input < "0" or user_input > str(num_ace):
                raise ValueError
            return int(user_input)

        except ValueError:
            print("Wrong input please try again| values in range")
            return self.Calculate_total_ace()


        
        