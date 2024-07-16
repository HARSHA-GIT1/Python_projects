#THIS PROGRAM IS HOW OPERATOR OVERLOADING WORKS...
#NOTE:-1.As name overloading means over+load (take work or actions unexcepated).
#      2.In this program we see two case.
#CASE-1
print(1+2)
print('1'+'2')
#Or
print(int.__add__(1,2))
print(str.__add__('1','2'))
#Case-1 is an example of operator overloading.

#CASE-2
class Complex_no:
    def __init__(self,r,i):
        self.Real=r
        self.imaginary=i
    #operator overloading
    def __add__(self,other):
        return f'{self.Real+other.Real}+{self.imaginary+other.imaginary}i'
        #print(f'{self.Real+other.Real}+{self.imaginary+other.imaginary}i')

c1=Complex_no(1,2)
c2=Complex_no(3,3)
#print(c1+c2)#here we get error because interpreator not know about that + which add two objects.
#But
#print(f'Answer using operator overloading:-{c1}+{c2}i')
print(c1+c2)