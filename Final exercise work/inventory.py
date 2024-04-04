from game import *

class Inventory:

    def __init__(self):
        self.games = {
            1: Game("The Witcher 3", "RPG"),
            2: Digitalgame("Stardew Valley", "Farm RPG"),
        }

    def subtract_game(self, title, amount):
        game_found = False
        for game_key, game in self.games.items():
            if game.title == title and game.qty >= int(amount):
                game.qty -= int(amount)
                print(f"order completed! {game.qty} available copies of {game.title} left")
                game_found = True
            elif game.title == title and game.qty < int(amount):
                print("not enough copies available")
                game_found = True
            
        if not game_found:
            print(f"{title} is not in our inventory")
    
    def add_game(self, game):
        game_key = self.gen_key()
        self.games[game_key] = game


    def gen_key(self):
        max_key = max(self.games)
        return max_key + 1

inv = Inventory()

    
