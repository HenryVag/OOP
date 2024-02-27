#File name: Exercise_4.5.py
#Author: Henry Våg
#Description: Exercise 4.5

class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")



class SecretMagicPotion(MagicPotion):

    def __init__(self,name: str, password: str):
        self.__password = password
        super().__init__(name)

    def add_ingredient(self, ingredient: str, amount: float, entered_password: str = None):
        if entered_password == self.__password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Incorrect password")

    # Why have default value??
    def print_recipe(self, entered_password: str):
        if entered_password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Incorrect password")


diminuendo=SecretMagicPotion("Diminuendo maximus","hocuspocus")
diminuendo.add_ingredient("Toadstool",1.5,"hocuspocus")
diminuendo.add_ingredient("Magic sand",3.0,"hocuspocus")
diminuendo.add_ingredient("Frogspawn",4.0,"hocuspocus")
diminuendo.print_recipe("hocus")

