#File name: Exercise_4.8.py
#Author: Henry Våg
#Description: Exercise 4.8

class Task:

    id = 1

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.id
        Task.id += 1

    def __str__(self):
        return f"{self.id}: {self.description} {self.workload}, programmer {self.programmer} {"NOT FINISHED" if self.finished == False else "FINISHED"}"
    
    def is_finished(self):
        return False if self.finished == False else True
    
    def mark_finished(self):
        self.finished = True


"""
t1=Task("program hello world","Eric",3)
print(t1.id,t1.description,t1.programmer,t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2=Task("program webstore","Adele",10)
t3=Task("program mobile app for workload accounting","Eric",25)
print(t2)
print(t3)"""

class OrderBook:

    def __init__(self):
        self.tasks = {}
        