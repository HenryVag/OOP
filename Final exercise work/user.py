from validator import valid_amount
from game import *


class User:

    def __init__(self, name, password):
        self.id = 0
        self.name = name
        self.password = password
        self.balance = 0
        self.owned_games = {}

    def add_balance(self, amount):
        if valid_amount(amount):
            self.balance += amount

    def list_games(self):
        if not self.owned_games:
            print("")
            print("you have no games")
            print("")
        for game in self.owned_games.values():
            print(f"Name: {game.title}\nGenre: {game.genre}\nType: {game.type} \nQuantity:{game.qty}")
            print("")
    
    def add_game(self, title, genre, qty,  type):
        game = Digitalgame(title, genre, qty) if type == "y" else Game(title, genre, qty)
        if game not in self.owned_games:
            game_key = 0 if not self.owned_games else max(self.owned_games) + 1
            self.owned_games[game_key] = game