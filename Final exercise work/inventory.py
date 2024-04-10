#File name: inventory.py
#Author: Henry Våg
#Description: Contains the inventory and its functions of the video game store management system


from game import *

class Inventory:

    def __init__(self):
        self.games = {
            1: Game("The Witcher 3", "RPG"),
            2: Digitalgame("Stardew Valley", "Farm RPG"),
        }

    def list_games(self):
       for game_key, game in self.games.items():
            print(f"{game.title}, {game.type}")

    def subtract_game(self, title, amount, type):
        game_found = False
        if type == "y":
            type = "digital"
        if type == "n":
            type = "disc"
        for game_key, game in self.games.items():
            if game.title == title and game.qty >= int(amount) and game.type == type:
                game.qty -= int(amount)
                result = f"order completed! {game.qty} available copies of {game.title} {type} version left"
                game_found = True
            elif game.title == title and game.qty < int(amount) and game.type == type:
                result = "not enough copies available"
                game_found = True
            
        if not game_found:
            result = f"{title}, {type} version is not in our inventory"
        return result

    def add_game(self, game):
        if self.not_in_inv(game):
            game_key = self.gen_key()
            self.games[game_key] = game


    def gen_key(self):
        max_key = max(self.games)
        return max_key + 1
    
    def not_in_inv(self, game):
        for game_key, gam in self.games.items():
            if game.title == gam.title and game.type == gam.type:
                print("game already in inventory")
                return False
        return True

inv = Inventory()

    
