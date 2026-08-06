
class Player:
    '''Player class, define and money'''

    def __init__(self, money: int|None):
        '''Constructor to initialize user'''

        self.money = money if money and money >= 0 else 0 

    def bet(self):
        '''The player gets to bet'''
        pass

    

