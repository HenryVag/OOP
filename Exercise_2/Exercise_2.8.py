#File name: Exercise_2.8
#Author: Henry Våg
#Description: Exercise 2.8

class Checklist:

    def __init__(self, header,entries):
        self.header = str(header)
        self.entries = list(entries)


class Customer:

    def __init__(self, id, balance, discount):
        self.id = str(id)
        self.balance = float(balance)
        self.discount = int(discount)

class Cable:

    def __init__(self, model, length, max_speed, bidirectional):
        self.model = str(model)
        self.length = float(length)
        self.max_speed = int(max_speed)
        self.bidirectional = bool(bidirectional)




