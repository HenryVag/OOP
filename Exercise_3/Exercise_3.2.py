#File name: Exercise_3.2.py
#Author: Henry Våg
#Description: Exercise 3.2

class NumberStats:

    def __init__(self):
        self.numbers = []
        


    def add_number(self, input):
        self.numbers.append(input)

    def count_numbers(self):
        amount = len(self.numbers)
        return amount
    
    def get_sum(self):
        sum = 0
        for number in self.numbers:
            sum += int(number)
        return sum
    def average(self):
        sum = self.get_sum()
        if len(self.numbers) > 0:
            avg = sum/len(self.numbers)
        else:
            avg = 0
        
        return avg
    


def askfor_input(stats,even,odd):
    user_in = input("Enter integer:")

    if user_in != "-1":
        stats.add_number(int(user_in))
        if int(user_in) % 2 == 0:
            even.numbers.append(user_in)
            askfor_input(stats,even,odd)
        else:
            odd.numbers.append(user_in)
            askfor_input(stats,even,odd)
    else:
        print("Sum of numbers",stats.get_sum())
        print("Mean of numbers:", stats.average())
        print("Sum of even numbers:", even.get_sum())
        print("Sum of odd numvers:", odd.get_sum())



def main():
    stats = NumberStats()
    even = NumberStats()
    odd = NumberStats()


    askfor_input(stats, odd, even)

main()


