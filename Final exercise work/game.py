


class Game:

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.price = 10
        self.qty = 100
        self.type = "disc"
    

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}\nType: {self.type}"



class Digitalgame(Game):
    def __init__(self, title, genre):
        super().__init__(title, genre)
        self.type = "digital"

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}\nType: {self.type}"
    


