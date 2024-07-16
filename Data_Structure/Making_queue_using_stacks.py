"""
IN THIS PROGRAM WE PERFORM QUEUING OPERATIONS USING 2-STACKS
"""
from Stack_for_queue import *
class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    #Make a Method For Insert The Data In Second Stack:-
    def insert_first(self):
         while not self.stack2.isempty():
                data = self.stack2.pop()
                self.stack1.push(data)

    #Make a Method For Insert The Data In Second Stack:-
    def insert_second(self):
        while not self.stack1.isempty():
            data = self.stack1.pop()
            self.stack2.push(data)

    #Make a Method For Getting Peek :-
    def peek(self):
            if self.stack1.isempty():
                print('Queue is Empty')
            else:
                self.insert_second()
                self.stack2.peek()
                self.insert_first()

    #Make a Method for enqueue:-
    def enqueue(self,value):
        self.stack1.push(value)

    #Make a Method for dequeue:-
    def dequeue(self):
        if self.stack2.isempty():
            if self.stack1.isempty():
                print('Queue is Empty')
            else:
                self.insert_second()#Insert into second stack.
                self.stack2.pop()
                self.insert_first()#Insert into first stack.

        else:
                self.insert_second()#Insert into second stack.
                self.stack2.pop()
                self.insert_first()#Insert into first stack.

    #Make a Method For Printing Queue:-
    def __str__(self):
        self.insert_second()
        result =''
        while not self.stack2.isempty():
            data = self.stack2.pop()
            result = result + str(data) +','
            self.stack1.push(data)
        return result[:-1]


#USING FROM THERE:-
queue = Queue()
queue.enqueue(12)
queue.enqueue(10)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(13)
queue.enqueue(15)
queue.enqueue(14)
queue.enqueue(9)
print(queue)
queue.peek()
queue.dequeue()
print(queue)
queue.peek()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
queue.peek()