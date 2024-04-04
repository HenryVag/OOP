from inventory import Inventory



class GameManager:
    
    def __init__(self, inv):
        self.inv = inv
    
    def order(self):
        print("Which game would you like to order?")
        title = input("Title:")
        amount = input("How many copies?:")
        self.inv.subtract_game(title, amount)





gamemgr = GameManager(Inventory())
