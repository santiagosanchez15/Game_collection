
class Player:
    '''Player class, shared functions'''

    def __init__(self):
        '''Constructor to initialize user'''
        self.selection = None

    def __eq__(self, other):
        return self.selection == other.selection

    def bet(self):
        '''The player gets to bet'''
        pass

    def choose_option(self):
        pass

