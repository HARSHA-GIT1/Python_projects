#THIS PROGRAM IS SHOW HOW METHOD-OVERLOADING WORK IN PYTHON...
#(i).In python method overloading is not support defaulty.
#(ii).But We can Achieve the method overloading using Multiple method.
#(iii).Just like default and *arg arguments.
#CASE-1
'''class Overload:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj=Overload()
Sum=obj.add(1,2)
print(Sum)'''
#But In Case-2
#CASE-2
#(i)Default Arguments
class Overload:
    def add(self,a,b,c=0):
        return a+b+c
    def add(self,a,b,c):
        return a+b+c
obj=Overload()
print(obj.add(1,2))
print(obj.add(1,2,4))
#(i)*Args
'''class Overload:
    def add(self,a,b):
        return a+b
    def add(self,*args):
        total=0
        for i in args:
            total=i+total
        return total
obj=Overload()
Sum=obj.add(1,2)
Sum= obj.add(1,2,3,4,5)
print(Sum)'''