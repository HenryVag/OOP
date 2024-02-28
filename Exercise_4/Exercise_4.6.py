#File name: Exercise_4.6.py
#Author: Henry Våg
#Description: Exercise 4.6

import random



class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.__result = []

    def roll_dice(self):
        
        self.__result = []
        self.__result.append(random.randint(1,self.sides))

    @property
    def show_result(self): 
        return self.__result
    

class Player:

    def __init__(self, name, player_id):

        self.name = name
        self.player_id = player_id
        self.dice = Dice(6)
        self.pet = None
    
    def __str__(self):
        return f"Name: {self.name} ID: {self.player_id} Pet: {self.pet}"
    
    def roll_dice(self):
        self.dice.roll_dice()

    def assign_pet(self, mammal):
        self.pet = mammal




class Mammal:

    def __init__(self, mammal_id, species, name, size, weight):
        self.mammal_id = mammal_id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

    def __str__(self):
        return f"Pet: {self.name}, Species: {self.species}"









def roll_dice_list(dice_list):
    rolled_dice = []
    for dice in dice_list:
        dice.roll_dice()
        rolled_dice.append(dice.show_result[0])
    return rolled_dice



def calculate_winner(player1_rolls, player2_rolls):


    player1_score = 0
    player2_score = 0

    for roll in player1_rolls:
        player1_score += int(roll)

    for roll in player2_rolls:
        player2_score += int(roll)


    if player1_score > player2_score:
        return "Player1"
    elif player1_score == player2_score:
        return None
        
    else:
        return "Player2"


def create_dice_list(no_of_dice):
    return [Dice(6) for _ in range(no_of_dice) ]



def play_game(player1, player2):

    player1_rolls = roll_dice_list(player1)
    player2_rolls = roll_dice_list(player2)

    

    print(player1_rolls)
    print(player2_rolls)
    winner = calculate_winner(player1_rolls, player2_rolls)

    if winner:
        print(f"{winner} is the winner")
    else:
        print("Its a tie, rolling again...")
        play_game(player1, player2)


def main():
    no_of_dice = int(input("Enter number of dice:"))
    num_players = int(input("Enter number of players"))
    
    #player1  = create_dice_list(no_of_dice)
    #player2  = create_dice_list(no_of_dice)
    players = {}

    pets = [
        Mammal(1, "Cat","Indy", "Small", 5),
        Mammal(2, "Dog", "Vuokko", "Medium", 18),
        Mammal(3, "Dog", "Sini", "Medium", 16)
        ]
    
    for i in range(num_players):
        player_id = i + 1
        player_name = input(f"Enter player {player_id}'s name")
        player = Player(player_name, player_id)

        players[player_id] = player
    
    
    for player_id, player in players.items():
        if no_of_dice == 2:
            pet_dice_rolls = sum(roll_dice_list(create_dice_list(2)))
            if pet_dice_rolls <= 4:
                player.assign_pet(pets[0])
            elif 4 < pet_dice_rolls <= 8:
                player.assign_pet(pets[1])
            else:
                player.assign_pet(pets[2])
        else:
            player.roll_dice()
            print(f"{player}: Dice Rolls - {player.dice.show_result}")

    #Prints every player and their pet
    """        
    for player_id, player in players.items():
            
        print(f"Player: {player.name} {player.pet}")
    """
    
    
    #play_game(player1, player2)

if __name__ == "__main__":
    main()