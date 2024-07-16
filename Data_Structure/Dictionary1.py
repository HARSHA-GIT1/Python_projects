"""
In This Program ,We Make a Dictionaries Class For Performing Dictionaries Operations and Using Hashing
(Linear-Probing)
Issue:-Here First Issue Comes using condition(Stopping to increase size of Dictionary) that is can't change the
value of insert key.
"""
#Make a class For Dictionaries
class Dictionary:
    def __init__(self,size):
        self.size = size
        self.Condition =size
        #Make Two List for Key and Data
        self.key = [None]*size
        self.data = [None]*size

    #Make a Method For Put Data Into Dictionary:-
    def put(self,key,value):
        if self.Condition >0:
            hash_value = self.hash(key)
            #First Check Key list is empty
            if self.key[hash_value] is None:
                self.data[hash_value] = value
                self.key[hash_value] = key
            else:
                #Check key is already exists
                if self.key[hash_value] == key:
                    self.data[hash_value] = value
                else:
                    #If Data is New Go ahead till find None Index
                    new_hash = self.rehash(hash_value)
                    #In While Loop we Also Check Key is Already exists
                    while self.key[new_hash] is not None and self.key[new_hash] is not key:
                        new_hash= self.rehash(new_hash)

                    if self.key[new_hash] is None:
                        self.key[new_hash] = key
                        self.data[new_hash] = value
                    else:
                        self.data[new_hash] = value

            #Reduced Condition
            self.Condition=self.Condition -1
        else:
            print('Dictionary Size Is Not Exceed')

    #Make a Method For Getting the element:-
    def get(self,key):
        #First Check Key Exists or Not
        Start_pos = self.hash(key)
        Current_pos = Start_pos
        while self.key[Current_pos] is not None:
            if self.key[Current_pos] is key:
                return f'{key}:{self.data[Current_pos]}'
            Current_pos = self.rehash(Current_pos)
            if Current_pos == Start_pos:
                return 'Item Not Found'
        return 'Item Not Found'

    #Make a Method For Rehashing the Hash Value
    def rehash(self,key):
        #Here We return a new index of list
        # Here We Use Absolute Function For Getting Always Positive-Index
        return abs((key+1)%self.size)

    #Make a Method For Calculating Hash Value:-
    def hash(self,key):
        # Here We Use Absolute Function For Getting Always Positive-Index
        return abs(hash(key)%self.size)

    #Make a Dunder Method For Insert Data:-
    def __setitem__(self, key, value):
        self.put(key,value)

    #Make a Dunder Method For Get Data:-
    def __getitem__(self, item):
       return self.get(item)
    #Make a Dunder Method For Print Dictionary:-
    def __str__(self):
        result =''
        for i in range(len(self.key)):
            if self.key[i] is not None:
                data =str(str(self.key[i])+":"+str(self.data[i]))
                result=result+data+','
        return '{'+result[:-1]+'}'