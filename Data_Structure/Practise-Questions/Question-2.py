"""QUES-2 Make a Method for Replacing a value with max-value in linklist
"""
#First Create a Node Class:-
class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None

#Create a class of linklist :-
class Linklist:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self,value):
        #Create a node:-
        new_node = Node(value)

        # Take address to Head
        new_node.next = self.head

        #Passing the Address To Head:-
        #self.head = id(new_node)# why not work ?
        self.head = new_node

        #Increase the Length of Linklist
        self.size = self.size+1

    def __str__(self):
        if self.head is None:
            return 'Linklist is empty'
        result = ''
        temp = self.head
        while temp is not None:
            result = result + str(temp.data) +'->'
            temp = temp.next
        return result[:-2]

    #Create a method for find the sum of all data at odd position:-
    def Sum_of_odd(self):
        if self.head is None:
            print('Linklist is Empty')
        else:
            temp = self.head
            pos = 1
            Sum = 0
            while temp is not None:
                if pos % 2 != 0:
                    Sum = Sum + temp.data
                temp = temp.next
                pos = pos+1
            print('Sum of all Element at Odd Position:-',Sum)
            
#Use of Linklist
L = Linklist()
L.insert(89)
L.insert(33)
L.insert(55)
L.insert(7)
L.insert(12)
L.insert(10)
L.insert(10)
L.insert(8)
print(L)
L.Sum_of_odd()
