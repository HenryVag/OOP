#File name: Exercise_2.6
#Author: Henry Våg
#Description: Exercise 2.6

import datetime

def list_years(dates: list):

    years = []
    years.append(date1.year)
    years.append(date2.year)
    years.append(date3.year)

    years.sort()
    return years
    


date1 = datetime.date(2019,2, 3)
date2 = datetime.date(2006, 10, 10)
date3 = datetime.date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)