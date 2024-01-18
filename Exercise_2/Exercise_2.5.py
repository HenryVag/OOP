#File name: Exercise_2.5
#Author: Henry Våg
#Description: Exercise 2.5

def smallest_average(person1: dict, person2: dict, person3: dict):

    def calculate_avg(person: dict):
        return(person["result1"] + person["result2"] + person["result3"])/3


    averages = {
        'person1': calculate_avg(person1),
        'person2': calculate_avg(person2),
        'person3': calculate_avg(person3)

    }
    
    min_person = min(averages, key = averages.get)

    if min_person == "person1":
        print(person1)
    elif min_person == "person2":
        print(person2)
    else: 
        print(person3)

   

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

smallest_average(person1, person2, person3)