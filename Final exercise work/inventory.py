from game import *

class Inventory:

    def __init__(self):
        self.games = {
            "witcher3": Game("The Witcher 3", "RPG"),
            "stardew valley": Game("Stardew Valley", "Farm RPG"),
        }

    def subtract_game(self, title, amount):
        for game_key, game in self.games.items():
            if game.title == title:
                game.qty -= int(amount)
                print(game.qty)
                


inv = Inventory()

    
