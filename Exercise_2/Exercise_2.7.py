#File name: Exercise_2.7
#Author: Henry Våg
#Description: Exercise 2.7

class Manga:

    def __init__(self, name, author, genre, release_year):

        self.name = name
        self.author = author
        self.genre = genre
        self.release_year = release_year

berserk = Manga("Berserk","Miura", "Seinen", "1990")

print(f"{berserk.author}: {berserk.name} ({berserk.release_year})")