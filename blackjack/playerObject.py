
from random import choice

class Player():
    '''Class player, works for user and AI, brings basic implementation'''

    def __init__(self, name : str|None):

        self.FullDeck : list[str] = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #Get list of possible values
        self.ValueCards : dict[str, int] = { #Create value reference table
            "1": 1,
            'A': 11, 
            "2": 2, 
            "3":3, 
            "4": 4, 
            "5":5, 
            "6":6, 
            "7":7,
            "8":8, 
            "9":9,
            "10":10, 
            "J":10, 
            "Q":10, 
            "K":10
            }
        
        self.deck : list[str] = [] #crate empty deck
        self.ValueDeck : int = 0
        self.Name : str = name if name else "Player" #Give value for matters of interactivity

    def Intial_Draw(self):
        '''Get initial two cards and prints them out'''

        self.deck.append(choice(self.FullDeck)) #Get first Card
        self.deck.append(choice(self.FullDeck)) #Get Second Card
        self.Print_Cards() #Print cards

    def Print_Cards(self):
        print("The cards in your deck are:\n")
        for card in self.deck:
            print(f"  -{card}")

    def Get_Total(self):
        pass

    def get_Card(self):
        pass

    def is_over21(self):
        '''Returns true if deck is over 21'''

        return self.Get_Total > 21