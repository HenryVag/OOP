


class Game:

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.price = 10
        self.qty = 100
    

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}"



class Digitalgame(Game):
    def __init__(self):
        self.type = "digital"
        super().__init__(self)

    def __str__(self):
        return f"Name: {self.title}\nGenre: {self.genre}\nType: {self.type}"
    


