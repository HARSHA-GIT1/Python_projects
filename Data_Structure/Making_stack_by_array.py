"""
IN THIS PROGRAM WE MAKE A STACK USING AN ARRAY
"""
class Stack:
    #This Constructor use for create array(Fixed) and initialize top:-
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.stack = [None]*self.size

    #Make a Method for Push Operation:-
    def push(self,value):
        if self.top >=self.size-1:
            print('Stack_overflow')
        else:
            self.top = self.top + 1
            self.stack[self.top] = value

    # Make a Method for Pop Operation:-
    def pop(self):
        if self.top <=-1:
            print('Stack_underflow')
        else:
             data = self.stack[self.top]
             self.top = self.top - 1
             print(f'You deleted {data} from top or {self.top+1} position')

    #Make a Method for printing stack:-
    def __str__(self):
        result = ''
        for i in range(self.size-1,-1,-1):#Run Loop Reverse For getting Top
            result = result+str(self.stack[i])+','
        return result[:-1]

    #Make a Method for getting peek data:-
    def peek(self):
        print(self.stack[self.top])
s = Stack(4)
s.push(12)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
s.push(1)
print(s)
s.peek()
