#File name: Exercise_4.2.py
#Author: Henry Våg
#Description: Exercise 4.2

class Item:

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __str__(self):
        return(f'Name: {self._name} Weight: {self._weight}g')

    def name(self):
        return self._name
    
    def weight(self):
        return f'{self._weight}g'




book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
print("Name of the book:",book.name())
print("Weight of the book:",book.weight())
print("Book:",book)
print("Phone:",phone)



