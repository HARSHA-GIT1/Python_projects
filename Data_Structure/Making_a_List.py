#THIS PROGRAM IS MAKING A LIST ANF ALSO PERFORM ITS FUNCTIONS(LIKE append, delete , print, etc)...
import ctypes  # This Module is used c datatypes

class MyList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A = self.create_array(self.size)

    @staticmethod
    #Making a function for creating an array:-
    def create_array(size):
        #Creating a List Using size
        return (size*ctypes.py_object)()

    #Making a function which return len of list:-
    def __len__(self):
        return self.n

    #Making a function which append the list:-
    def append(self,item):
        if self.n == self.size:
            #Resize
            self.resize(self.size*2)

        self.A[self.n]=item
        self.n = self.n+1

    #Making a function for resizing the array:-
    def resize(self,capacity):
        #creating an array
        B=self.create_array(capacity)
        self.size=capacity
        #copy the value to new array
        for i in range(self.n):
            B[i]=self.A[i]
        #Resign
        self.A=B

    # Using Dunder Method Printing a List:-
    def __str__(self):
        result=''
        for i in range(self.n):
            result= result+ str(self.A[i])+','#Here We Make an Array List...
        return "["+result[:-1]+"]"

    # Using Dunder Method Getting Data Using Index.
    def __getitem__(self, index):
        # Working For Negative Indexing:-
        if index < 0:
            index = self.n+index
            if index >=0: #(Means n-index != 0)
              return self.A[index]
            else:
                return "Index Out of Range"

        elif 0 <= index < self.n:
            return self.A[index]

        else:
            return "Index Out Of Range"

    # Making a Function For Pop The Item From Array:-
    def pop(self):
        if self.n == 0:
            print("Empty List")
        else:
            Data=self.A[self.n-1]
            self.n = self.n -1
            print(Data)
    # Making a Function For Clear The Item Of Array:-
    def clear(self):
        if self.n == 0:
            print("List Already Empty")
        else:
            self.n = 0
            self.size = 1

    #Making a Function For Getting The Element Index in List:-
    def find(self,data):
        if self.n==0:
            return 'Empty List'
        else:
            for i in range(self.n):
                if data == self.A[i]:
                    return i
                """else:
                    if i == self.n-1:
                        print("Element Not Exists")"""
            return 'Value Not Exists'

    #Making a Function For Insert The Data At Special or Determine Location:-
    def insert(self,index,data):
        if self.n == self.size:
            #resize
            self.resize(self.size*2)

        #Extend The Array Or Adjust The Element
        for i in range(self.n,index,-1):
            self.A[i]=self.A[i-1]

        self.A[index]=data
        self.n = self.n+1

    #Making a Function For Deleting an Element in List:-
    def __delitem__(self, key):
        #Delete.
        if 0<= key >=self.n:
            print('Index Out of Range')

        else:
            self.A[key] = 0
            for i in range(key,self.n-1):
                self.A[i]=self.A[i+1]
            self.n = self.n -1

    #Making a Function For Removing an Element in List:-
    def remove(self,data):
        result=self.find(data)
        if type(result)== int:
            #delete
           self.__delitem__(result)
        else:
            print(result)

    #Making a Function For Sorting a Dynamic Array or List:-

    def sort(self):
        for i in range(self.n):
            for j in range(i+1,self.n):
                if int(self.A[i]) > int(self.A[j]):
                    temp = self.A[i]
                    self.A[i] = self.A[j]
                    self.A[j] = temp


    """#Making a max function for return a max value
    def __max__(self,data):
        temp_list=[]
        for i in range(self.n):
            if type(data[i]) == int:
                temp_list.append(int(data[i]))
            else:
                return "We can't > between str and int"
        result = temp_list.sort()
        return result[self.n-1]
"""

    #Making a Function For Count:-
    def count(self,value):
        result=self.find(value)
        if type(result) == int:
            return result
        else:
            return 0

    #Making a Function For Extending The List:-
    def extend(self,data):
        temp = len(data)
        for i in range(temp):
            if self.n == self.size:
                # resize
                self.resize(self.size * 2)
            self.A[self.n] = data[i]
            self.n = self.n +1

    #Making a Function For Performing Sum Operation:-
    @staticmethod
    def __sum__(data):
        temp = len(data)
        Total=0
        for i in range(temp):
            Total+= int(data[i])
        return Total