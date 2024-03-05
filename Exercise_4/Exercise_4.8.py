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
        self.tasks = []


    def add_order(self, description, programmer, workload):
        new_task = Task(description, programmer, workload)
        self.tasks.append(new_task)

    def all_orders(self):
            return self.tasks
    
    def programmers(self):
        programmers = []
        for task in set(self.tasks):
            programmers.append(task.programmer)
        
        return list(set(programmers))
    
    def mark_finished(self, id:int):
        
        for task in self.tasks:
            if task.id == id:
                if not task.finished:
                    task.finished = True
                    break
                else: 
                    print(f"Task {task.id} is already finished")
                    break
        else:
            raise ValueError("Task not found")
        
    def finished_orders(self):
        finished_tasks = []
        for task in self.tasks:
            if task.finished == True:
                finished_tasks.append(task)
        return finished_tasks
    
    def unfinished_orders(self):
        unfinished_tasks = []
        for task in self.tasks:
            if task.finished == False:
                unfinished_tasks.append(task)
        return unfinished_tasks

    def status_of_programmer(self, programmer: str):
        finished_tasks = 0
        unfinished_tasks = 0
        workload_finished_tasks = 0
        workload_unfinished_tasks = 0

        for task in self.tasks:
            if task.programmer == programmer and task.finished:
                finished_tasks += 1
                workload_finished_tasks += task.workload
            elif task.programmer == programmer and not task.finished:
                unfinished_tasks += 1
                workload_unfinished_tasks += task.workload
        return finished_tasks, unfinished_tasks, workload_finished_tasks, workload_unfinished_tasks

     
orders=OrderBook()
orders.add_order("program webstore","Adele",10)
orders.add_order("program mobile app for workload accounting","Adele",25)
orders.add_order("program app for practising mathematics","Adele",100)
orders.add_order("program the next facebook","Eric",1000)

orders.mark_finished(1)
orders.mark_finished(2)

"""
for order in orders.all_orders():
    print(order)


for task in orders.finished_orders():
    print(task)


for task in orders.unfinished_orders():
    print(task)
"""
status=orders.status_of_programmer("Adele")
print(status)

"""    
for programmer in orders.programmers():
    print(programmer)
    """


