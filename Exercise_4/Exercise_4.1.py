from collections import Counter



class ListHelper:

    @staticmethod
    def greatest_frequency(my_list: list):
        #Can only count max item of list where there is 1 maximum occurence
        occurrences = Counter(my_list)
        mc = max(occurrences.values())
        for pair in occurrences.items():
            
            if pair[1] == mc:
                return f' The most common item in the list is {pair[0]} with {pair[1]} occurrences'
            
            
    @staticmethod
    def doubles(my_list: list):
        unique_items = 0
        occurrences = Counter(my_list)
        for pair in occurrences.items():
            if pair[1] > 1:
                unique_items += 1
        return f'There are {unique_items} items that occur more than twice'
        




numbers = [1,1,2,1,3,3,4,5,5,5,6,5,5,5]

print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))