"""
Question:-5 Make a Method for Delete Duplicate value in Sorted link-list
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

            # Create a node:-
            new_node = Node(value)

            # Check List is Empty or Not
            if self.head is None:
                self.head = new_node
                self.size = self.size + 1
                return

            # searching the list
            temp = self.head
            while not temp.next is None:
                temp = temp.next

            # Take address to current node
            temp.next = new_node

            # Increase the Length of List:-
            self.size = self.size + 1

    def Traverse(self):
        if self.head is None:
            print( 'Linklist is empty' )

        result = ''
        temp = self.head
        while temp is not None:
            result = result + str(temp.data)+','
            temp = temp.next
        print(result[:-1])

    #Make a Method for Sorting the Linklist(Ascending-Order):-
    def sort_List(self):
        out_temp = self.head
        #Outer loop
        while out_temp is not None:
            in_temp = out_temp.next
            #Inner-Loop
            while in_temp is not None:
                if out_temp.data > in_temp.data:
                    temp = out_temp.data
                    out_temp.data = in_temp.data
                    in_temp.data = temp
                in_temp = in_temp.next
            out_temp = out_temp.next

    #Make a Method for Delete Duplicate element:-
    def delete_dupli(self):
        temp = self.head
        #Outer Loop
        """while temp is not None:
            in_temp = temp
            #Inner Loop
            while in_temp is not None:
                if in_temp.next is not None and temp.data == in_temp.next.data :
                    in_temp.next = in_temp.next.next
                in_temp = in_temp.next"""

        #It Reduced Complexity
        while temp is not None:
            if temp.next is not None and temp.next.data == temp.data:
                temp.next = temp.next.next
            temp = temp.next
L = Linklist()
L.insert(20)
L.insert(3)
L.insert(0)
L.insert(2)
L.insert(10)
L.insert(200)
L.insert(20)
L.insert(2)
L.insert(3)
L.insert(200)
L.Traverse()
L.sort_List()
L.Traverse()
L.delete_dupli()
L.Traverse()
