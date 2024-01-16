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
            self.sideup = "Heads"

        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup
    
#Main function definition
    

def main():

    my_coin = Coin()

    print("This side up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())
#Calling main function
    
main()


