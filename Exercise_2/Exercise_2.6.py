#File name: Exercise_2.6
#Author: Henry Våg
#Description: Exercise 2.6

import datetime

def list_years(dates: list):

    new_list = [date.year for date in dates]
    
    return sorted(new_list)

    

    
date1 = datetime.date(2019,2, 3)
date2 = datetime.date(2006, 10, 10)
date3 = datetime.date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)