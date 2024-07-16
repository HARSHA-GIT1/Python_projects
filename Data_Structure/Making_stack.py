"""THIS PROGRAM IS SHOWING THE WORKING OF STACK(LIFO)
(1). Here we can make a stack using linklist and array both.
(2). Now we make using linklist
"""
#Make a class for Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Make a class for Stack
class Stack:
    def __init__(self):
        self.top = None

    #Make a method for check stack is empty or not:-
    def isempty(self):
        return self.top is None

    #Make a method for insert data in stack:-
    def push(self,value):
        #Make a new-Node
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    #Make a method for Traverse:-
    def traverse(self):
        if self.isempty():
            print('Stack is Empty')
        else:
            temp = self.top
            result = ''
            while temp is not None:
                result = result + str(temp.data) + ','
                temp = temp.next
            print(result[:-1])

    #Make a method for Pop Operation:-
    def pop(self):
        if self.isempty():
            print('Stack is Empty')
        else:
            self.top = self.top.next

    #Make a method for getting top or peek operation:-
    def peek(self):
        if self.isempty():
            print('Stack is Empty')
        else:
            print(self.top.data)

    #Make a method for getting the no of elements in stack:-
    def count(self):
        if self.isempty():
            print('Stack is Empty')
        else:
            tem = self.top
            count = 0
            while tem is not None:
                count = count + 1
                tem = tem.next
            print(count)
