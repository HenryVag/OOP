#File name: Exercise_4.2.py
#Author: Henry Våg
#Description: Exercise 4.2

class Item:

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    
    def __str__(self):
        return(f'Name: {self._name} Weight: {self._weight}g')

    @property
    def name(self):
        return self._name
    @property
    def weight(self):
        return f'{self._weight}'



"""
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
print("Name of the book:",book.name)
print("Weight of the book:",book.weight)
print("Book:",book)
print("Phone:",phone)

book.weight = 100

"""

class Suitcase:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []

    def __str__(self):
        if len(self.items) == 1:
            return(f"{len(self.items)} item ({self.total_weight})g")
        else:
            return(f"{len(self.items)} items ({self.total_weight})g")


    def add_item(self, item):

        if int(item.weight) <= int(self.max_weight) - int(self.weight()):
            self.items.append(item)
            print("Item added")
        else:
            print("Item not added")

    def print_items(self):
        for item in self.items:
            print(item)
    
    def weight(self):
       total_weight = 0
       for item in self.items:
           total_weight += int(item.weight)
       return total_weight
    
    def heaviest_item(self):
        i = 0
        heaviest_item = self.items[0]
        
        while i < len(self.items)-1:
            if int(self.items[i+1].weight) > int(heaviest_item.weight):
                heaviest_item = self.items[i+1]
            i += 1
        if not self.items:
            return heaviest_item
        else:
            return "No items"

         





"""
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
suitcase=Suitcase(500)
print(suitcase)
suitcase.add_item(book)
print(suitcase)
suitcase.add_item(phone)
print(suitcase)
suitcase.add_item(brick)
print(suitcase)
"""

"""
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
suitcase=Suitcase(1000)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)
print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight=suitcase.weight()
print(f"Combined weight:{combined_weight}g")

heaviest=suitcase.heaviest_item()
print(f"The heaviest item:{heaviest}")
"""

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cargo = []

    def __str__(self):
        if len(self.cargo) == 1:
            return(f"{len(self.cargo)} suitcase, space for {self.weight_remaining()}kg")
        else:
            return(f"{len(self.cargo)} suitcases, space for {self.weight_remaining()}kg")
    
    def weight_remaining(self):
        cargo_weight = sum(suitcase.weight() for suitcase in self.cargo)
        return self.max_weight - (cargo_weight / 1000)



    def add_suitcase(self, suitcase):
        self.cargo.append(suitcase)

    def print_items(self):
        for suitcase in self.cargo:
            suitcase.print_items()
        

        

"""
cargo_hold=CargoHold(100)
print(cargo_hold)
book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
adas_suitcase=Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase=Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)
cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)"""

book=Item("ABC Book",200)
phone=Item("Nokia 3210",100)
brick=Item("Brick",400)
adas_suitcase=Suitcase(1000)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)
peters_suitcase=Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold=CargoHold(100)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)
print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()