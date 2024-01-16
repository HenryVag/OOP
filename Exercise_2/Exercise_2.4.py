#File name: Exercise_2.4
#Author: Henry Våg
#Description: Exercise 2.4

import math

def factorials(n: int):

    factorials_dict = {}

    i = 1
    while (i < n+1):
        factorial_value = math.factorial(i)
        factorials_dict[i] = factorial_value
        i = i + 1
    return factorials_dict

k = factorials(5)

print(k[1])
print(k[3])
print(k[5])

