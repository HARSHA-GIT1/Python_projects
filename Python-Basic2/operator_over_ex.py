#THIS PROGRAM IS BASED ON A EXCERCISE ON OPERATOR OVERLOADING..
class Persons:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age>other.age:
            return True
        else:
            return False
p1=Persons('Harsh Vardhan Gupta',19)
p2=Persons('Tushar Gupta',21)
if p1>p2:
    print(p1.name,'Pay the Bill')
else:
    print(p2.name,'Pay the Bill')