#THIS PROGRAM IS SHOWING HOW MAGIC OR DUNDER OPERATOR WORKS...
#(i).Basically We Use This Type Of Operator in Operator Overloading..
#(ii).There is multiple dunder method avaiable.
#(a).
'''class Dunder:
    def __init__(self,a):
        self.first=a
    def __add__(self, other):
        return f'Addition ={self.first+other.first}'
obj1=Dunder(1)
obj2=Dunder(2)
print(obj1+obj2)
'''
#(b).
'''class Dunder:
    def __init__(self,a):
        self.first=a
    def __add__(self, other):
        return f'Addition ={self.first+other.first}'
    def __lt__(self, other):
        if self.first<other.first:
            return True
        else:
            return False
obj1=Dunder(1)
obj2=Dunder(2)
print(obj1+obj2)
print(obj1>obj2)
'''
#(c).
class Dunder:
    def __init__(self,a):
        self.first=a
    def __len__(self):
        return len(self.first)
obj1=Dunder("Harsh Vardhan Gupta")
print(len(obj1))