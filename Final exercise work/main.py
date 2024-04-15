#File name: main.py
#Author: Henry Våg
#Description: The main function for a simplified video game store system


from game_manager import gamemgr
from validator import valid_command


def main():
    # Main function to run the program
    while True:
        commands()
        command = input("command:")
        if command == "1":
            if gamemgr.login():
                while True:
                    user_commands()
                    user_command = input("command:")
                    if user_command == "0":
                        gamemgr.logout()
                        print("logged out")
                        break
                    else:
                        execute_command(user_command)
            
        if command == "2":
            gamemgr.create_user()
        if command == "0":
            break
            

def commands():
    # Displaying main menu commands
    print("")
    print("login or create user")
    print("--------------------")
    print("exit - 0")
    print("login - 1")
    print("create user - 2")
    

def user_commands():
    # Displaying commands for logged in user
    print("commands:")
    print("---------")
    print("0 - log out")
    print("1 - order")
    print("2 - list available games")
    print("3 - add new game")
    print("4- list your games")
    

def execute_command(command):
    # Executes user commands
    if valid_command(command):
        if command == "1":
            gamemgr.order()
        if command == "2":
            gamemgr.list_games() 
        if command == "3":
            gamemgr.add_new_game()
        if command == "4":
            gamemgr.user_list_games()
    
    


# Starts main program
if __name__ == "__main__":
    main()