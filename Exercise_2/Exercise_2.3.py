#File name: Exercise_2.3
#Author: Henry Våg
#Description: Exercise 2.3

from datetime import datetime
import time

class alarm:
    def __init__(self):
        
        self.model = "rolex"
        self.saved_time = "00:00"
        self.alarm_set = False
        self.alarm_time = None
        self.alarm_volume = "1"

    

    def clock(self):

        while True:
            self.new_time_check()
            


    def new_time_check(self):

        if self.previous_time_check(self.saved_time) == True:
            current_time = datetime.now()
            print(current_time.strftime("%H:%M"))
            self.saved_time = current_time.strftime("%H:%M")
            if self.alarm_set == False:
                self.set_alarm()
            elif self.alarm_set == True:
                self.activate_alarm()
                self.delete_alarm()
                


    def previous_time_check(self, saved_time):
        
        current_time = datetime.now().strftime("%H:%M")
        if saved_time < current_time:
            return True
        
    def set_alarm(self):
        self.alarm_time = input("Input the time for your alarm (h:min):")
        if self.alarm_time != "":
            self.alarm_set = True
        self.alarm_volume = input("Input the alarm volume 1-low 2-high:")

    def delete_alarm(self):
        if self.alarm_time != "":
            print("Current alarm", self.alarm_time)
            user_input = input("Do you want to delete the current alarm? y/n")
            if user_input == "y":
                self.alarm_time = ""
                print("Alarm deleted succesfully")

    
    def activate_alarm(self):
        current_time = datetime.now().strftime("%H:%M")
        if str(self.alarm_time) == str(current_time):
            if self.alarm_volume == "1":
                print("alarm")
            elif self.alarm_volume == "2":
                print("ALARM")
            
        
        
            
def main():

    test = alarm()
    test.clock()

main()