#THIS PROGRAM IS SHOWING THE WORKING OF LINKLIST....
#Create a node class for creating a particular node :-
class Node:
    def __init__(self,data):
        self.data =  data
        self.add = None

#Create a class of linklist :-
class Linklist:

    def __init__(self):
        self.head = None
        self.size = 0

    #Make a function for getting length of linklist:-
    def  __len__(self):
        return self.size

    #{ INSERT-FUNCTIONS START }

    #Make a function for insert the data at starting in linklist:-

    def insert_head(self,value):
        #Create a node:-
        new_node = Node(value)

        # Take address to Head
        new_node.add = self.head

        #Passing the Address To Head:-
        #self.head = id(new_node)# why not work ?
        self.head = new_node

        #Increase the Length of Linklist
        self.size = self.size+1

    # Make a function for insert the data at end in linklist:-

    def insert_end(self,value):
        # Create a node:-
        new_node = Node(value)

        #Check List is Empty or Not
        if self.head is None:
            self.head = new_node
            self.size = self.size + 1
            return

        #searching the list
        temp = self.head
        while not temp.add is None:
            temp = temp.add

        # Take address to current node
        temp.add = new_node

        #Increase the Length of List:-
        self.size = self.size +1

    # Make a function for insert the data after the value in linklist:-
    def insert_after(self,value,data):
        if self.head is None:
            print('Linklist is empty')

        else:
            temp = index= self.head
            #Searching the value
            while not temp is None:
                if temp.data == value:
                    index = temp
                    break
                temp = temp.add

            if index.data == value:
                #create a new node
                 new_node = Node(data)
                 self.size = self.size + 1
                 #Passing the address of next node after new node
                 new_node.add = index.add
                 #Passing the address of new node
                 index.add = new_node
            else:
                print('value is not exists')

    # Make a function for insert the data before the value in linklist:-
    def insert_before(self, value, data):
        if self.head is None:
            print('Linklist is empty')

        else:
            temp = index = self.head
            # Searching the value
            while not temp is None:
                if temp.add.data == value:#here we check the value node before it.
                    index = temp
                    break
                temp = temp.add

            if index.add.data == value:
                 # create a new node
                 new_node = Node(data)
                 self.size = self.size+1
                 # Passing the address of next node after new node
                 new_node.add = index.add
                 # Passing the address of new node
                 index.add = new_node
            else:
                 print('value is not exists')

    #{ DELETE-FUNCTION START }

    #Make a function for clear the Linklist:-
    def clear(self):
        if self.head is None:
            print('Linklist is already empty')
        else:
            self.head = None

    #Make a function for deleting from head:-
    def delete_from_head(self):
        if self.head is None:
            print('Linklist is empty')
        else:
            #Store the value
            value = self.head.data
            #Transfer add of next node to head
            self.head = self.head.add
            self.size = self.size-1
            print('Deleted data is:',value)

    # Make a function for deleting from tail:-
    def delete_from_Tail(self):
        if self.head is None:
            print('Linklist is empty')

        else:
            #Here first check that we have a single node or not
            if self.size == 1:
                self.delete_from_head()

            else:
                temp = self.head
                while not temp.add.add is None:
                    temp = temp.add

                # Store the value
                value = temp.add.data
                # Give None add to current node
                temp.add = None
                self.size = self.size - 1
                print('Deleted data is:', value)

    # Make a function for deleting a node after value contain node:-
    def delete_By_value_after(self,value):
        if self.head is None:
            print('Linklist is empty')

        else:
            temp = index = self.head
            # Searching the value
            while not temp is None:
                if temp.data == value:  # here we check the value node before it.
                    index = temp
                    break
                temp = temp.add

            if index.data == value:
                #Passing the address of deleted next node
                data = index.add.data
                index.add = index.add.add
                self.size = self.size - 1
                print('Deleted data is:',data)
            else:
                print('value is not exists')

    # Make a function for deleting a node after value contain node:-
    def delete_By_value_before(self, value):
        if self.head is None:
            print('Linklist is empty')

        else:
            temp = index = self.head
            # Searching the value
            while not temp is None:
                if temp.add.add.data == value:  # here we check the value node before it.
                    index = temp
                    break
                temp = temp.add

            if index.add.add.data == value:
                # Passing the address of deleted next node
                data = index.add.data
                index.add = index.add.add
                self.size = self.size - 1
                print('Deleted data is:',data)
            else:
                print('value is not exists')

    #Making a Function which delete the node using indexing
    def __delitem__(self, key):
        # Check index range
        if key > self.size:
            print('Index out of range')
        elif self.head is None:
            print('Linklist is empty')
        elif key == 0:
            self.delete_from_head()
        else:
            # Create a variable for getting the position of node
            temp_count = 0
            temp = self.head
            while temp.add is not None:
                if temp_count+1 == key:
                    break
                temp_count = temp_count + 1  # Increase Position
                temp = temp.add

            #deleting the node
            del_data = temp.add.data
            temp.add = temp.add.add
            self.size = self.size - 1
            print('Deleted data is ',del_data,'from index',key )
    #SEARCHING FUNCTIONS STARTS:-

    #Make a function for searching by value:-
    def search_by_value(self,value):
        if self.head is None:
            print('Linklist is empty')
        else:
            #Create a variable for getting the position of value contain node
            temp_count=0
            temp = self.head
            while temp.add is not None:
                if temp.data == value:
                    break
                temp = temp.add
                temp_count = temp_count + 1  # Increase Position
            if temp.data == value:
                print(f'Node {temp_count} Contain {value} and Its address is {id(temp)}')
            else:
                print('Value Not exists')

    # Make a function for searching by :-index
    def __getitem__(self, item):
        #Check Index Exists or Not
        if item > self.size:
            return 'Index out of range'
        if self.head is None:
            return 'Linklist is empty'
        else:
            # Create a variable for getting the position of value contain node
            temp_count = 0
            temp = self.head
            while temp.add is not None:
                if temp_count == item:
                  return  f'Node {item} Contain {temp.data} data and Its address is {id(temp)}'
                  temp = temp.add
                  temp_count = temp_count + 1  # Increase Position

            return 'Value Not exists'

    #Make a function for traversing or printing a linklist:-
    def __str__(self):
        if self.head is None:
            return 'List is empty'
        else:
            curr = self.head
            result = ''
            while not curr is None:
                result = result + str(curr.data)+'->'
                curr = curr.add
            return result[:-2]