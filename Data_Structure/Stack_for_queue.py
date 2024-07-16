#THIS PROGRAM IS FOR MAKING A STACK CLASS FOR MAKING A QUEUE:-
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

    #Make a method for Pop Operation:-
    def pop(self):
        if self.isempty():
            return
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    #Make a method for getting top or peek operation:-
    def peek(self):
        if self.isempty():
            return
        else:
            print(self.top.data)