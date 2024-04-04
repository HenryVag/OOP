from inventory import Inventory
from game import Game, Digitalgame


class GameManager:
    
    def __init__(self, inv):
        self.inv = inv
    
    def order(self):
        print("Which game would you like to order?")
        title = input("Title:")
        amount = input("How many copies?:")
        self.inv.subtract_game(title, amount)

    def list_games(self):
        for game_key, game in self.inv.games.items():
            print(game.title)

    def add_new_game(self):
        print("-----------")
        title = input("title:")
        genre = input("genre:")
        type = input("digital y/n?:")
        if type == "y":
            game = Digitalgame(title, genre)
        if type == "n":
            game = Game(title, genre)
            
        self.inv.add_game(game)


gamemgr = GameManager(Inventory())
