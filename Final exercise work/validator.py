#File name: validator.py
#Author: Henry Våg
#Description: Validator functions for the application



def valid_command(command):
    if command.isdigit() and 0 <= int(command) <= 3:
        return True
    else:
        print("invalid input, please try again")


def valid_game(title, genre, type):
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
    if len(title) <= 20:
        return True
    else:
        print("title too long")

    

def valid_genre(genre):
    if len(genre) <= 10:
        return True
    else:
        print("invalid genre")
    

def valid_type(type):
    if type == "y" or type == "n":
        return True
    else:
        print(f"{type} is not an accepted value")