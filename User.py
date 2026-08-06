from . import Player
from check_amount import check_add_amount

class User(Player):
    '''User class, get to choose what to use, add money and check if has enough money'''

    def __init__(self, money:int|None, name:str="USER"):
        '''Constrcutor for user player'''

        super().__init__()
        self.money = money
        self.name = name

    def __repr__(self):
        '''Return USER description, money, current_selection and name'''
        return f"This is {self.name}, this player has {self.money} and the players last selection was {self.selection}"

    def add_money(self):
        amount_add:str = input("How much money do you wish to add to your account")
        amount_int: int = self.check_add_amount(amount_add) #get amount to add


    def check_add_amount(self, amount:str) -> int:
        if amount == "":
            print("No input...")
             if self.keep_playing() ####FIXME getting to ahead of time this will be the palyer function to go between the games
        total_amount:list = []
        
        for char in amount:
            if char >= "0" and char <= "9":
                total_amount.append(char)
            elif char == "-":
                total_amount.append(char)

        try: ## check if no money added
            if len(total_amount) <= 0:
                raise  ValueError("No money added")
        except ValueError as e:
            print(f"ERROR {e}")
            return -1 
        return int("".join(total_amount))

    
    def keep_playing(self)-> bool:
        '''Gets user ingput and return if keep playing or not'''
        user_input:str = input("Do you wish to keep playing yes/no: ")
        return self.check_yes_no(user_input)


    def check_yes_no(input:str)-> bool:
        '''Check if input is yes or no'''
            
        try: 
            if input.lower() == "yes":
                    return True
            elif input.lower() == 'no':
                    return False
            print(f"Wrong input {input} is not an option")
            raise ValueError

        except ValueError:
            return keep_playing()



  