#File name: Exercise_1.py
#Author: Henry Våg
#Description: Exercise 1 of the OOP course

import random
"""
#1.

print("Hello")


#2.

my_list = []


while len(my_list) < 10:
    user_input = input("Input integers:")
    my_list.append(user_input)

print(str(my_list)[1:-1])

my_list_str = []

while len(my_list_str) < 10:
    user_input = input("Input string:")
    my_list_str.append(user_input)
print(str(my_list_str)[1:-1])


my_list.clear()

while len(my_list) < 10:
    n = random.randint(1,10000)
    my_list.append(n)

print(my_list)

#3.


my_list.sort()
print(my_list)


my_list_str.sort()
print(my_list_str)


#4.

lst = []

def read_integers():
    
    user_input = input("Enter integer:")
    check_for_0(user_input)
   


def negative_int_count():
    #Counts number of negative integers in list
    negative_count = 0
    i = 0
    while i < len(lst):
        if lst[i][0] == "-":
            negative_count = negative_count + 1
            i = i+1
        else:
            i = i+1
    print("Number of negative integers:", negative_count)

def even_int_count():
    #Counts amount of even numbers
    even_count = 0
    i = 0
    while i < len(lst):
        if int(lst[i]) % 2 == 0:
            even_count = even_count + 1
            i = i+1
        else:
            i = i+1
    print("Number of even integers:", even_count)

def div_by3_count():
    div3_count = 0
    i = 0
    while i < len(lst):
        if int(lst[i]) % 3 == 0 and int(lst[i])>= 0:
            div3_count = div3_count + int(lst[i])
            i = i + 1
        else:
            i = i + 1
    print("Sum of positive integers divisible by 3:", div3_count)
    

    

def check_for_0(user_input):
    #Checks for correct user input and starts calculation of negative numbers
    if user_input != "0" and user_input.isalpha() == False:
        lst.append(user_input)
        read_integers()
    if user_input == "0":
        print("Stopping program")
        negative_int_count()
        even_int_count()
        div_by3_count()
    if user_input.isalpha() == True:
        print("No letters allowed")
        read_integers()
    

read_integers()
        



def number_of_terms(ap_max):
    
    if int(ap_max) >= 0:
        term_count = int(ap_max)//3
        procession(term_count)
        print("Number of terms",term_count)
    if int(ap_max) < 0:
        term_count = 0
        procession(term_count)
        print("Number of terms", term_count)
   



def procession(term_count):
    terms = []
    i = 3

    while len(terms) < term_count:
        terms.append(i)
        i = i+3
    print("Procession:", terms)
    sum_of_terms(terms)

def sum_of_terms(terms):
    summed_terms = sum(terms)
    print("Sum of terms",summed_terms)
    sum_of_squares(terms)

def sum_of_squares(terms):
    
    sum_of = 0
    i = 0
    while i < len(terms):
        term = int(terms[i])
        sum_of = sum_of + term**2
        i = i + 1
    print("Sum of squares:", sum_of)



def ap_main():
    ap_max = input("Enter the maximum value of the progression:")
    if ap_max.isalpha() == False:
        number_of_terms(ap_max)
        
        


ap_main()


#8.

def rps_main():
    
    
    # Rock = 1, Paper = 2, Scissors = 3
    print("Welcome to rock-paper-scissors!")
    

    winner()

def cpu_input():
    choice = random.randrange(1,4)
    return choice

def winner():
    
    cpu_wins = 0
    user_wins = 0
    print("Rock = 1, Paper = 2, Scissors = 3")
    while cpu_wins < 3 or user_wins < 3:

        user_input = input("What will you fight with?")
        choice = cpu_input()

        win_conditions = {
        
        '1': '3', # Rock beats scissors
        '2': '1', # Paper beats rock
        '3': '2'  # Scissors beat paper
        }
        
        if user_input == str(choice):
            print("Tie")
            
        elif win_conditions[user_input] == str(choice):
            print("You win!")
            user_wins +=1
            print("Computer",cpu_wins, "You", user_wins )
            
        else: 
            print("You lose")
            cpu_wins += 1
            print("Computer",cpu_wins, "You", user_wins )
            

        if user_wins == 3:
            print ("You won the game!")
            print("Computer",cpu_wins, "You", user_wins )
            break
        if cpu_wins == 3:
            print("You lost the game")
            print("Computer",cpu_wins, "You", user_wins )
            break

rps_main()



#9.

def return_random():

    random_value = random.randrange(1,7)

    return random_value


print("Random number:", return_random())


"""
#10.

def phonebook_main():

    people = {}

    while True:
    
        user_input = input("1 - Search, 2 - Add, 3 - Quit")

        if user_input == "3":
            print("Shutting down...")
            break

        while True:
            if user_input == "1":
                search(people)
                break
                
            if user_input == "2":
                add(people)
                break
        
            

def search(people):
    name = input("Name:")

    if name in people:
        print("--------------")
        print("Name:", name)
        print("Phonenumber:", people[name])
        print("--------------")

    else:
        print("Name not found")
        phonebook_main()

def add(people):

    print("--------------")
    add_name = input("Input name:")
    add_number = input("Add number:")
    print("--------------")

    if check_inputs(add_name, add_number, people) == True:
        people[add_name] = add_number
        print("Name and phonenumber added successfully")
            
    else:
        print("Submitted values are incorrect")
        
            
def check_inputs(add_name, add_number, people):
    
    name_bool = False
    number_bool = False
    
    if add_name.isalpha() == True:
        name_bool = True

    if add_number.isalpha() == False and add_number not in people.values():
        number_bool = True
    
    if number_bool == True and name_bool == True:
        return True 
        
    else:
        return False
    
phonebook_main()

