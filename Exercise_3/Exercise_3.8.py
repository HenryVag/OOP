#Author: Henry Våg
#File name: Exercise_3.8.py
#Description: Exercise 3.8

class Recording:

    def __init__(self, __length: int):
        
        self.__length = __length

    def __str__(self):
        return f'{self.__length}'
    
    @property
    def length(self):
        return f'{self.__length}'
    @length.setter

    def length(self, new_length):
        self.__length = new_length


the_wall =Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)