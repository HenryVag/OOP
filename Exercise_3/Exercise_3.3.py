#Author: Henry Våg
#File name: Exercise_3.2.py
#Description: Exercise 3.2

class LunchCard:

    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner
    
    def __str__(self):
        return str(self.balance)
    
    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95
        else:
            print("You cannot afford this")
    
    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90
        else:
            print("You cannot afford this")

    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError ("Sike, that's the wrong number")
        else:
            self.balance += deposit

        
        

def main():
    card1 = LunchCard(20, "Peter")
    card2 = LunchCard(30, "Grace")

    card1.eat_luxury()
    card2.eat_ordinary()

    print(f'{card1.owner}:', "The balance is:", card1.balance)
    print(f'{card2.owner}:', "The balance is:", card2.balance)

    card1.deposit_money(20)
    card2.eat_luxury()

    print(f'{card1.owner}:', "The balance is:", card1.balance)
    print(f'{card2.owner}:', "The balance is:", card2.balance)

    card1.eat_ordinary()
    card1.eat_ordinary()

    card2.deposit_money(50)

    print(f'{card1.owner}:', "The balance is:", card1.balance)
    print(f'{card2.owner}:', "The balance is:", card2.balance)



main()