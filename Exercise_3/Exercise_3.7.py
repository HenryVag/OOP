#Author: Henry Våg
#File name: Exercise_3.7
#Description: Exercise 3.7

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name



class Room:

    person_lst = []

    def __init__(self):
        pass

    @staticmethod
    def add(person: Person):
        Room.person_lst.append(person)

    @staticmethod
    def is_empty():
        if len(Room.person_lst) == 0:
            return True
        else:
            return False
        
    @staticmethod    
    def combined_height():
        combined_height = 0
        for person in Room.person_lst:
            combined_height += person.height
        return combined_height


    @staticmethod
    def print_contents():
        print(
            f'There are {len(Room.person_lst)} people in the room and their ' \
            f'combined height is {Room.combined_height()}cm')
        for person in Room.person_lst:
            print(f'{person.name} ({person.height})')

    @staticmethod
    def shortest():
        
        if Room.is_empty() == True:
            return None
        else:
            shortest_person = Room.person_lst[0]
            for person in Room.person_lst:
                if person.height < shortest_person.height:
                    shortest_person = person
                
            return shortest_person
        
    @staticmethod
    def remove_shortest():
        if Room.is_empty() == False:
            shortest_person = Room.shortest()
            Room.person_lst.remove(shortest_person)
            return shortest_person
        else:
            return None
        



room =Room()
print("Is the room empty?", room.is_empty())

room.add(Person("Lea",183))
room.add(Person("Kenya",172))
room.add(Person("Ally",166))
room.add(Person("Nina",162))
room.add(Person("Dorothy",175))

print("Is the room empty?",room.is_empty())
room.print_contents()

print("Shortest:",room.shortest())

removed =room.remove_shortest()

print(f"Removed from room: {removed.name}")

room.print_contents()