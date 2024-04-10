#File name: game_manager.py
#Author: Henry Våg
#Description: Interacts with the modules according to main.py

from inventory import Inventory
from game import Game, Digitalgame
from validator import *

class GameManager:
    
    def __init__(self, inv):
        self.inv = inv
    
    def order(self):
        print("Which game would you like to order?")
        title = input("Title:")
        amount = input("How many copies?:")
        type = input("Which type? y = digital / n = disc:")
        print(self.inv.subtract_game(title, amount, type))

    def list_games(self):
        self.inv.list_games()

    def add_new_game(self):
        print("-----------")
        title = input("title:")
        if valid_title(title):
            genre = input("genre:")
            if valid_genre(genre):
                type = input("digital y/n?:")
                if valid_type(type):

                    if type == "y":
                        game = Digitalgame(title, genre)
                    if type == "n":
                        game = Game(title, genre)

                    self.inv.add_game(game)


gamemgr = GameManager(Inventory())
