"""QUES-1 Make a Method for Replacing a value with max-value in linklist
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

    #Create a method for replace a value with max value:-
    def replace_max(self,value):
        temp = self.head
        Max = temp
        while temp is not None:
           if temp.data >= Max.data:
               Max = temp
           temp = temp.next
        Max.data = value

    """def replace_with(self):
        if self.head is None:
            return 'Linklist is empty'

        temp = self.head
        max_value = 0
        while temp is not None:
            print('Enter in Outer Loop')
            print('Max value =', max_value)
            #create a variable for inner loop
            inner_temp = temp.next

            while inner_temp is not None:
                print('Enter in Inner Loop')
                print('Max value =',max_value)
                if max_value > temp.data or max_value > inner_temp.data:
                    print('max is great')
                    break
                elif temp.data >= inner_temp.data:
                     print('temp.data is great')
                     max_value = temp.data
                else:
                    print('inner.data is great')
                    max_value = temp.next.data
                print('\n\n\n')
                inner_temp = inner_temp.next
            temp = temp.next
        print(max_value)"""
#Use of Linklist
L = Linklist()
L.insert(89)
L.insert(33)
L.insert(55)
L.insert(7)
L.insert(12)
L.insert(0)
L.insert(10)
L.insert(8)
print(L)
L.replace_max(19)
print(L)