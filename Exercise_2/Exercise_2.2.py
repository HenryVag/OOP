#File: Exercise_2.2
#Source: Tony Gaddis, Starting out with python, fourth edition
#Modified by: Henry Våg
#Description: Coin object and tossing

import random

#Class definition

class Coin:

    def __init__(self):

        self.sideup = "Heads"

    def toss_the_coin(self):
        if random.randint(0,1) == 0:
            if self.toss_or_event() == True:
                self.sideup = "Heads"
            else:
                self.random_event()

        else:
            if self.toss_or_event() == True:
                self.sideup = "Tails"
            else: 
                self.random_event()

    def get_sideup(self):
        return self.sideup
    
    def random_event(self):
        eventnum = random.randint(0,2)
        if eventnum == 0:
            self.sideup = "Coin lands on the table upright"
        elif eventnum == 1:
            self.sideup = "Coin drops on the ground and disappearsin a rabbit hole"
        else:
            self.sideup = "Coin defies gravity and gets lost on a wormhole in space"


    def toss_or_event(self):
        if random.randint(0,1) == 0:
            return True
        
        else:
            self.random_event()
        
    
#Main function definition
    

def main():

    my_coin = Coin()

    print("This side up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    
    if my_coin.get_sideup() == "Heads":
        print("Now this side is up:", my_coin.get_sideup())
    elif my_coin.get_sideup() == "Tails":
        print("Now this side is up:", my_coin.get_sideup())
    else: 
        print(my_coin.get_sideup())
#Calling main function
    
main()


