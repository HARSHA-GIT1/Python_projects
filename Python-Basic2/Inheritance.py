#THIS PROGRAM IS SHOWING THE WORKING OF INHERITANCE...
#Example-1
"""class animal:#Parent class
    def Eat(self,name):
        print(name,'Is Eating Food')
    def Bath(self,name):
        print(name,'Bathing')
class Dog(animal):#Child Class
    pass
dog=Dog()
dog.Eat('Jerry')
dog.Bath('Juli')"""
#Example-2
class Student:
    def __init__(self,name,marks):
        self.Name=name
        self.Marks=marks

    def Intro(self):
        print(f'Mr {self.Name} You work Hard')

    def Display(self):
        print(f'Hii, {self.Name} Your Marks Is {self.Marks}')

class Harsh(Student):
    def __init__(self):
        print('hello')
    def Intro(self):
        print('You are Coder')
        '''print('You are Coder')#Here Function Overridding'''
        '''#Super Function
        super().Intro()
        print('You are Coder')'''
#obj1=Harsh('Harsh Vardhan Gupta',200)
obj1=Harsh()
#obj1.Display()
obj1.Intro()
