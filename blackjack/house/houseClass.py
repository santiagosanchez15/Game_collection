import sys
import os
from random import choice
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playerClass.playerObject import Player


class House(Player):
    '''House object to play blackjack'''

    def __init__(self, name : str |None):
        super().__init__(name=name) #Get previews values form parent class

    def Intial_Draw(self):
        '''Initial Draw for player'''

        self.deck.append(choice(self.FullDeck)) #Get first Card

        #FIXME check if value is Ace


        self.deck.append(choice(self.FullDeck)) #Get Second Card
        self.Calculate_total_deck() #Calculate totals

    def Calculate_total_deck(self):
        '''Calculate the total of the deck'''

        self.ValueDeck = sum(self.ValueCards[card] for card in self.deck)

    def Add_card_deck(self, card:str):
        '''Add given card to deck'''
        self.deck.append(card)
        self.Calculate_total_deck() #Recalculate total

