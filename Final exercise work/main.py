from game_manager import gamemgr



def main():
   while True:
    commands()
    command = input("command:")
    if command == "0":
        break
    else:
        execute_command(command)

def commands():
    print("commands:")
    print("---------")
    print("0 - exit")
    print("1 - order")
    print("2 - list games")
    print("3 - add new game")

def execute_command(command):
    if command == "1":
       gamemgr.order()
    if command == "2":
       gamemgr.list_games() 
    if command == "3":
       gamemgr.add_new_game()
    
    




if __name__ == "__main__":
    main()