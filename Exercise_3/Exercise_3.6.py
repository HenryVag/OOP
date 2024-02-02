#Author: Henry Våg
#File name: Exercise_3.6.py
#Description: Exercise 3.6

class Present:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name} ({self.weight}g)'
       


book = Present("Harry Potter", 100)

print("The name of the present", book.name)
print("The weight of the present:",book.weight)
print("Present:",book)


class Box:

    def __init__(self ):
        self.presents = {}

    def add_present(self, present: Present):
        self.presents[present.name] = present

    def total_weight(self):
        total_weight = 0
        for present_name, present in self.presents.items():
            total_weight += present.weight
        return total_weight


box = Box()
box.add_present(book)
cd =Present("Pink Floyd: Dark Side of the Moon",50)
box.add_present(cd)

vhs =Present("Star Wars: A new hope",300)
box.add_present(vhs)

print(box.total_weight())