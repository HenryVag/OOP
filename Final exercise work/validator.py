#File name: validator.py
#Author: Henry Våg
#Description: Validator functions for the application



def valid_command(command):
    #Checks if command is digit and within range
    if command.isdigit() and 0 <= int(command) <= 4:
        return True
    else:
        print("invalid input, please try again")


def valid_game(title, genre, type):
    # Validates game title, genre and type
    if valid_title(title):
        if valid_genre(genre):
            if valid_type(type):
                return True
            else: 
                print(f"${type} is not an accepted value")
        else:
            print("invalid genre")
    else: 
        print("title too long")

def valid_title(title):
    # Checks if title length is within range
    if 1 <= len(title) <= 20:
        return True
    else:
        print("invalid title")

    

def valid_genre(genre):
    # Checks if genre length is within range
    if 1 <= len(genre) <= 10:
        return True
    else:
        print("invalid genre")
    

def valid_type(type):
    # Validates type of game
    if type == "y" or type == "n":
        return True
    else:
        print(f"{type} is not an accepted value")

def valid_amount(amount):
    # Validates quantity added
    if isInt(amount) or isFloat(amount) and amount < 200:
        return True
    else:
        print("please enter a valid number")

    def isInt(amount):
        if amount.isdigit():
            return True
    
    def isFloat(amount):
        try:
            float(amount)
            return True
        except ValueError:
            return False