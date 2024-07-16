#THIS PROGRAM IS SHOWING THE WORKING OF MULTIPLE INHERITANCE...
#CASE-1 and CASE-2 Show How Same Functions Is Called

#CASE-1
print('CASE-1')

class Father:#Parent 1
    def Intro(self):
        print('I can Eat')
        print('My sex is Male')
        print('I Have Money')
    def Work(self):
        print('I am Work in Out ')
class Mother:#Parent 2
    def intro(self):
        print('I can Eat')
        print('My sex is Female')
        print('I Have a power of Saving Money')
    def Work(self):
        print('I am Work in Home')
#class Son(Father,Mother):#Child
#   pass
#No2
class Son(Mother,Father):
    pass
obj1=Son()
obj1.Intro()
obj1.Work()#There We Get Father Work Function Not Mother For Get Mother Function Go to No 2

print()
print()
print()
print('CASE-2')
#CASE-2

class Father:#Parent 1
    def Intro(self):
        print('I can Eat')
        print('My sex is Male')
        print('I Have Money')
    def Work(self):
        print('I am Work in Out ')
class Mother:#Parent 2
    def intro(self):
        print('I can Eat')
        print('My sex is Female')
        print('I Have a power of Saving Money')
    def Work(self):
        print('I am Work in Home')
class Son(Father,Mother):#Child
   pass
obj1=Son()
obj1.Intro()
obj1.Work()
#OR
Mother.Work(obj1)

#CASE_3 and CASE_4 Tell About How we call multiple Constructor...

#CASE-3
print()
print()
print('CASE-3')
class Father:#Parent 1
    def __init__(self):
        self.Money=20000
        self.Health=80
    def Intro(self):
        print('I can Eat')
        print('My sex is Male')
        print('I Have Money')
    def Work(self):
        print('I am Work in Out ')
class Mother:#Parent 2
    def __init__(self):
        self.Love = 100
        self.Health = 70
    def intro(self):
        print('I can Eat')
        print('My sex is Female')
        print('I Have a power of Saving Money')
    def Work(self):
        print('I am Work in Home')
class Son(Father,Mother):#Child
   pass
obj1=Son()
print(obj1.Health,obj1.Money)
#print(obj1.Love)
#CASE-4
print()
print()
print('CASE-4')
class Father:#Parent 1
    def __init__(self,name):
        self.Money=20000
        self.Name=name
    def Intro(self):
        print('I can Eat')
        print('My sex is Male')
        print('I Have Money')


    def Work(self):
        print('I am Work in Out ')
class Mother:#Parent 2
    def __init__(self,name,language):
        self.Love = 100
        self.name = name
        self.Language=language
    def intro(self):
        print('I can Eat')
        print('My sex is Female')
        print('I Have a power of Saving Money')
    def Work(self):
        print('I am Work in Home')
class Son(Father,Mother):#Child
   def __init__(self,name,Name,language):
       Mother.__init__(self,name,language)
       Father.__init__(self,Name)
   def Display(self):
        print(f'Hii I am a {self.Language} Developer and My Mother Name is {self.name} and Father Name is {self.Name} ')

obj1=Son("Sonia Gupta","Sunit Kumar Gupta","Python")
#print(obj1.Money,obj1.Name)
#rint(obj1.Love,obj1.name,obj1.Language)
obj1.Display()