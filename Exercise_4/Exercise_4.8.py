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
        self.accepted_names_list = ["nina", "eric", "jonah", "adele", "henry", "elviira"]

    def add_order(self, description, programmer, workload):
        
        if programmer in self.accepted_names_list and workload.isdigit():
            new_task = Task(description, programmer, workload)
            self.tasks.append(new_task)
            return True
        else:
            return False

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
                if task.finished == False:
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
                workload_finished_tasks += int(task.workload)
            elif task.programmer == programmer and not task.finished:
                unfinished_tasks += 1
                workload_unfinished_tasks += int(task.workload)
        return finished_tasks, unfinished_tasks, workload_finished_tasks, workload_unfinished_tasks
    
    def add_accepted_name(self, name):
        if name not in self.accepted_names_list:
            self.accepted_names_list.append(name)
            print("name added")
        else: 
            print("name already accepted")



class OrderBookApplication:
    def __init__(self):
        self.__order_book = OrderBook()

    def run(self):
        

        while True:
            print("")
            self.commands()
            command = input("command:")
            if command == "0":
                break
            elif command == "1":
                description = input("description:")
                programmer = input("programmer:")
                workload = input("workload:")
                if self.__order_book.add_order(description, programmer, workload) and len(self.__order_book.tasks) < 50:
                    print("added!")
                else:
                    print("erroneus input")
            elif command == "2":
                for task in self.__order_book.finished_orders():
                    print(task)
            elif command == "3":
                for task in self.__order_book.unfinished_orders():
                    print(task)
        
            elif command == "4":
                task_id = input("id:")
                if task_id.isdigit() and int(task_id) <= 50:
                    self.__order_book.mark_finished(int(task_id))
                    print("marked as finished")
                else:
                    print("erroneus input")
            elif command == "5":
                if len(self.__order_book.programmers()) > 0:
                    for programmer in self.__order_book.programmers():
                        print(programmer)
                else:
                    print("no programmers")
            elif command == "6":
                programmer = input("programmer:")
                status=self.__order_book.status_of_programmer(programmer)
                print(status)
            elif command == "7":
                name = input("name:")
                if name.isalpha():
                    self.__order_book.add_accepted_name(name)
                else:
                    print("erroneous input")
            else:
                print("not a command")
        
            


    def commands(self):
        print("commands:")
        print("---------------------------")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print("7 add accepted name\n")

    
    

def main():
    
    orders = OrderBookApplication()
    orders.run()


if __name__ == "__main__":
    main()














