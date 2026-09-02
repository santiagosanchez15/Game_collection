import sys
import os
from random import choice
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playerClass.playerObject import Player


class House(Player):
    '''House object to play blackjack'''

    def __init__(self, name : str |None):
        self.new_ace : bool = False #Controls whether or not ace needs to be recalculated
        super().__init__(name=name) #Get previews values form parent class

    def Intial_Draw(self):
        '''Initial Draw for player'''

        card : str= self.check_next_move(choice(self.FullDeck)) #get first pseudo random card and check for value
        self.Add_card_deck(card) #add value to deck

        card = self.check_next_move(choice(self.FullDeck)) #get second pseudo random card and check for value
        self.Add_card_deck(card) #add value to deck

    def Recalculate_total(self):
        '''Calculate the total of the deck'''
        self.ValueDeck = sum(self.ValueCards[card] for card in self.deck)

    def get_Card(self):
        '''House decide whether or not to take another card'''

        #Check if house should play
        self.keep_playing()
        if self.wantsCard is False: return  #return if keep palying is false

        card : str = choice(self.FullDeck) #get a random card from deck

        if self.is_ace(card) is False: #Check if card is ace, if not add it to the deck and add value
            self.Add_card_deck(card)
            self.recalculate_ace()
            return 

        card = self.choose_value_ace(card) #get value ace
        self.Add_card_deck(card) #add card to deck and add to the total value
        self.recalculate_ace()

    def keep_playing(self): #FIXME check this function not convienced about this algorithm
        '''Decide if the house should grab another card '''

        # I think its easier to return True than all the cases for false
        if self.ValueDeck <= 17 and '11' in self.deck: 
            self.wantsCard = True
            return 

        if self.ValueDeck == 17 and '11' in self.deck and '6' in self.deck: #Check if value is 17 and 11 and 6 in deck, cant those two card in the same deck without pointing to value
            self.wantsCard = True
            return 

        if self.ValueDeck < 16: # if totalvalue is less than 16 then dealer takes another card
            self.wantsCard = True
            return

        self.wantsCard = False 

    #Ace functions
    
    def num_ace_inDeck(self) -> int:
        '''Returns number of Ace in deck'''
        return self.deck.count("11") + self.deck.count("1")#Get num ace in deck

    def has_ace(self):
        '''return true if ace present in deck'''
        return True if "11" in self.deck or "1" in self.deck else False

    def is_ace(self, card) -> bool:
        '''Return true if is ace'''
        return card == 'A'

    def choose_value_ace(self) -> str:
        '''Get value of ace either 1 or 11'''

        if self.ValueDeck + 11 <= 21: #check future value if value is less than 21 then add 11
            return "11"
        
        return '1' 

    def check_next_move(self, card : str) -> str:
        '''depending on the card returns card or returns value of ace'''

        if self.is_ace(card) is False: return card

        return self.choose_value_ace()

    def recalculate_ace(self) -> bool:
        '''Returns true if ace need to be recalculated else returns false'''

        
        if self.ValueDeck > 21 and ("11" in self.deck and self.ValueDeck - 10 <= 21):  #check if the value is greater than 21 and 11 in deck, and recalculate
            index : int = self.deck.index("11") #get index
            self.deck[index] = "1" #change values
            self.Recalculate_total() #recalcualte new total
            return True

        return False #FIXME i probably not need the return booleans


    def is_over_21(self) -> bool:
        '''Check if over 21, if so, check if can recalculate ace, if not, then return false'''      

        if self.ValueDeck <= 21: return False #Check if deck is less than or equal to 21, if so then false

        if self.recalculate_ace() is True: return False #check if can recalcualte ace, if so it does it return False as that value was recalcalculated
        return True #Cant do anything house over 21


    


        
    

