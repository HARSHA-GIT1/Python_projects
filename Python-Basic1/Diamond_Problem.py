#THIS PROGRAM IS SHOWINF THE WORKING OF DIAMOND PROBLEM....
'''#CASE-1
class A:
    def Display(self):
        print('Hello I am From Class A')

class B(A):
    def Display(self):
        print('Hello I am From Class B')
    def Show(self):
        print('Hello Ji')

class C(A):
    def Display(self):
        print('Hello I am From Class C')

class D(B,C):
    pass
Obj = D()
Obj.Display()
'''
#CASE-2
class A:
    def Display(self):
        print('Hello I am From Class A')

class B(A):
    def Display(self):
        print('Hello I am From Class B')
    def Show(self):
        print('Hello Ji')

class C(A):
    def Display(self):
        print('Hello I am From Class C')

class D(C,B):
    pass
Obj = D()
Obj.Display()