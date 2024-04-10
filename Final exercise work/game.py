#File name: game.py
#Author: Henry Våg
#Description: Contains class definitions for a game and its child class


class Game:

    def __init__(self, title, genre, qty):
        self.title = title
        self.genre = genre
        self.price = 10
        self.qty = 1
        self.type = "disc"
    

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}\nType: {self.type}"



class Digitalgame(Game):
    def __init__(self, title, genre, qty):
        super().__init__(title, genre,qty)
        self.type = "digital"

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}\nType: {self.type}"
    


