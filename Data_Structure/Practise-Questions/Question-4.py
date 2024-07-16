"""QUES-3 Make a Method to return a new string that is created by
#appending all  the characters given in the linked list as per the rules given below.
#Rules:-
1.Replace '*' or'/' by a single space
2.In case of two consecutive occurrences of '*' or '/' ,replace those
two occurrences by a single space and
convert the next character to upper case
3.The linked list will always end with an alphabet
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
            result = result + str(temp.data)
            temp = temp.next
        print( result)

    def String(self):
        if self.head is None :
            print('Linked List is empty')
        else:
            temp = self.head
            while temp is not None:
                if temp.data == '*' or temp.data == '/':
                    temp.data = ' '
                    if temp.next.data =='*' or temp.next.data =='/':
                            temp.next.next.data = temp.next.next.data.upper()
                            temp.next = temp.next.next

                temp = temp.next

#Use of Linklist
L = Linklist()
L.insert('A')
L.insert('n')
L.insert('*')
L.insert('/')
L.insert('a')
L.insert('p')
L.insert('p')
L.insert('l')
L.insert('e')
L.insert('*')
L.insert('a')
L.insert('/')
L.insert('d')
L.insert('a')
L.insert('*')
L.insert('*')
L.insert('k')
L.insert('e')
L.insert('e')
L.insert('p')
L.insert('s')
L.insert('/')
L.insert('*')
L.insert('a')
L.insert('/')
L.insert('/')
L.insert('d')
L.insert('o')
L.insert('c')
L.insert('t')
L.insert('o')
L.insert('r')
L.insert('*')

L.insert('A')
L.insert('w')
L.insert('a')
L.insert('y')
"""
L.insert('H')
L.insert('a')
L.insert('r')
L.insert('s')
L.insert('h')
L.insert('*')
L.insert('/')
L.insert('v')
L.insert('a')
L.insert('r')
L.insert('d')
L.insert('h')
L.insert('*')
L.insert('a')
L.insert('n')
"""
#print(L)
L.Traverse()
L.String()
L.Traverse()