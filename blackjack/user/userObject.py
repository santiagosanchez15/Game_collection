import sys
import os
from random import choice
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playerObject import Player

class User(Player):
    '''User class inherits from Player'''

    def __init__(self, name : str |None):

        super().__init__(name=name)

    def get_Card(self):
        '''Get a random card'''

        card : str = choice(self.FullDeck)
        self.deck.append(card)

    def Is_Ace(self, card:str) -> bool:
        '''Check if player got an ace, if so retrun true else no '''
        return card == "A"


    def num_ace_inDeck(self) -> int:
        '''Returns number of Ace in deck'''
        num_ace : int = self.deck.count("A") #Get num ace in deck
        print(f"You have {num_ace} Ace in your deck")
        return num_ace

    def Get_Total(self):
        return sum(lambda card : self.ValueCards[card] for card in self.deck) # sums all values of cards in deck #FIXME test that it works




        
        