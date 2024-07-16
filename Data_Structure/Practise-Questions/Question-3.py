"""QUES-3 Make a Method for Reversing the linklist
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

    def Traverse(self):
        if self.head is None:
            print( 'Linklist is empty' )
        result = ''
        temp = self.head
        while temp is not None:
            #result = result + str(temp.data) +'->'
            print(temp.data)
            temp = temp.next
        #print( result[:-2])

    #Creating a method for reverse the linklist:-
    def reverse(self):
        if self.head is None:
            print('Link-list is Empty')
        else:
            #create an attribute for getting next value of linklist-node
            Prev_node = Node
            Current_node = self.head
            while Current_node is not None:
                #Passing new node add
                Next_node = Current_node.next
                #Passing the add of previous node
                Current_node.next = Prev_node
                #Passing the add for previous node
                Prev_node = Current_node
                #Passing the add of next node to current node
                Current_node = Next_node
            self.head = Prev_node


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
#print(L)
L.Traverse()
L.reverse()
print('\n')
L.Traverse()