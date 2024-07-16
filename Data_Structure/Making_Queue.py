"""
THIS PROGRAM IS SHOWING THE WORKING OF QUEUE AND TELLS ABOUT HOW QUEUING FUNCTION WORKS.
"""
#Make a class for Node:-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Make a class for Queue:-
class Queue:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.count =0

    #Make a Method For Enqueue:-
    def enqueue(self,value):
        #First We create a new_node:-
        new_node = Node(value)
        self.count = self.count+1
        #Now check Queue is Empty or Not
        if self.Tail is None:
            self.Head = new_node
            self.Tail = self.Head
        else:
            self.Tail.next = new_node
            self.Tail = new_node

    # Make a Method For dequeue:-
    def dequeue(self):
       # Now check Queue is Empty or Not
            if self.Tail is None:
                print('List is Empty')
            else:
                self.count = self.count - 1
                data = self.Head
                self.Head = self.Head.next
                print(f'You pop {data}')

    # Make a Method For Peek:-
    def peek(self):
        print(self.Head.data)

    # Make a Method For Getting Length of Queue
    def __len__(self):
        return self.count

    #Make a Method For Print Data:-
    def __str__(self):
        #Check Empty or Not
        if self.Head is None:
            print('Queue is Empty')
        else:
            temp = self.Head
            result = ''
            while temp is not None:
                result = result + str(temp.data) + ','
                temp = temp.next
            return result[:-1]
