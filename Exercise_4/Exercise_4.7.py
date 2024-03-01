#File name: Exercise_4.7.py
#Author: Henry Våg
#Description: Exercise 4.7

class Phonebook:
    def __init__(self):
        self.__persons = {}

    def add_person_phonebook(self, new_person):
        if not new_person.name() in self.__persons:
            self.__persons[new_person.name()] = new_person

    def search_number(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_info(self):
        return self.__persons
    
    def search_name(self, name):
        if not name in self.__persons:
            return None
        return True

    def get_person_from_phonebook(self, name):
        if name in self.__persons:
            return self.__persons[name]
        else:
            return None

class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def add_number(self, number):
        print(f"Before appending {self.__numbers}")
        self.__numbers.append(number)
        print(f"After appending {self.__numbers}")

    def add_address_to_person(self, address): 
        self.__address = address

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address
    

class PhoneBookApplication:
    def __init__(self):
        self.__book = Phonebook()

    def instructions(self):
        print("commands: ")
        print("0 quit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        if self.__book.search_name(name):
            self.__book.__persons[name]["number"] = number
        else:
            new_person = Person(name)
            new_person.add_number(number)
            self.__book.add_person_phonebook(new_person)
            
        

    def search(self):
        name = input("name: ")
        person = self.__book.get_person_from_phonebook(name)
        
        if person is None:
            print("Person not found")
            return 

        if person.numbers():
            print(f"Number for {name}: {person.numbers()}")
        else:
            print("Number not available")
    
        address = person.address()
    
        if address:
            print(f"Address: {address}")
        else:
            print("Address not available")
        
               

    def add_address(self):
        name = input("name")
        address = input("address:")

        if self.__book.search_name(name):
            person = self.__book.get_person(name)
            person.add_address_to_person(address)
        else:
            new_person = Person(name)
            new_person.add_address_to_person(address)
            self.__book.add_person_phonebook(new_person)



    def run(self):
        self.instructions()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.instructions()


# test the code
application = PhoneBookApplication()
application.run()
                
