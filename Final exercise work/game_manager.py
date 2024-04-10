#File name: game_manager.py
#Author: Henry Våg
#Description: Interacts with the modules according to main.py

from inventory import Inventory
from game import Game, Digitalgame
from validator import *
from user import User

class GameManager:
    
    def __init__(self, inv):
        self.inv = inv
        self.users = {}
        self.logged_user = ""
    
    def order(self):
        print("Which game would you like to order?")
        title = input("Title:")
        genre = input("Genre:")
        qty = input("How many copies?:")
        type = input("Which type? y = digital / n = disc:")
        self.users[self.logged_user].add_game(title, genre, qty, type)
        print(self.inv.subtract_game(title, qty, type))

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
    
    def create_user(self):
        name = input("enter name:")
        if not self.name_in_use(name):
            password = input("enter password")         
            new_user = User(name, password) 
            if not self.users:
                new_key = 1
            else:
                new_key = max(self.users) + 1

            self.users[new_key] = new_user
            return True
        else:
            print("name already in use")
            return False
    
    def login(self):
        name = input("enter name:")
        password = input("enter password:")
        for user_key, user in self.users.items():
            if name == user.name and password == user.password:
                print("logged in")
                self.logged_user = user_key
                return True
        print("no matching username and password")
        return False
    
    def name_in_use(self, name):
        for user_key, user in self.users.items():
            if name == user.name:
                return True
        return False
    
    def user_list_games(self):
        user = self.users[self.logged_user]
        user.list_games()
            
gamemgr = GameManager(Inventory())
