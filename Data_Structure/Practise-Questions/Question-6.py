"""
Question-6 Write a python program for reverse a string using stack.
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
    def is_empty(self):
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

    #Make a method for Reverse a String:-
    def reverse_string(self,text):
       if self.top is None:
           print('')
       #write a loop for store value in stack
       for i in text:
           self.push(i)

       #write a loop for get reverse string
       temp = self.top
       result = ''
       while temp is not None:
           result = result + temp.data
           temp = temp.next
       print(result)

stack = Stack()
stack.reverse_string('hello')
