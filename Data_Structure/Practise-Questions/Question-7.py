"""
Question-7 Write a program for perform undo and redo operation
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

    """Make a method for check stack is empty or not:-"""
    def is_empty(self):
        return self.top is None

    #Make a method for insert data in stack:-
    def push(self,value):
        #Make a new-Node
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    #Make a Method for pop operation:-
    def pop(self):
        if self.is_empty():
            return
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    #Make a method for undo and redo operations:-
    @staticmethod
    def undo_and_redo(text, pattern):
        #Creates two Stacks
        u = Stack()
        r = Stack()
        #Convert data into string
        text = str(text)
        # Take a For Loop for Storing value:-
        for i in text:
            u.push(i)
        # Take a for Loop for undo and redo operations:-
        for i in pattern:
            if i == 'u':
                if not u.is_empty():
                    data = u.pop()
                    r.push(data)

            elif i == 'r':
                if not r.is_empty():
                    data = r.pop()
                    u.push(data)
            else:
                print('invalid code you pass ',i,'instead of u/r')
                return
        result = ''
        while not u.is_empty():
            result = str(u.pop()) + result
        print(result)

stack = Stack()
stack.undo_and_redo(1234,'ururu')