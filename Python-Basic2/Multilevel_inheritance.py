#THIS PROGRAM IS SHOW MULTILEVEL INHERITANCE WORK....
#Here Case -1 is Telling About How Methods Work in Multilevel-Inheritance
#CASE-1

'''print('CASE-1\n')
class GrandFather:
    def Intro(self):
        print('My Surname is Gupta')
        print('My Profession is Bussiness')
    def Work(self):
        print('I am Work For My Child')

class Father(GrandFather):
    def Work(self):
        print('I Am Work For Family')

class Son(Father):
    pass
obj1=Son()
obj1.Intro()
obj1.Work()
#OR
GrandFather.Work(obj1)
'''
#Now Case-2 is Telling About How __init__ Method Work in Multilevel Inheritance
#CASE-2

''''print('CASE-2\n')
class GrandFather:
    def __init__(self):
        self.Health=70
        self.Respect=100
        self.Money=300000

    def Intro(self):
        print('My Surname is Gupta')
        print('My Profession is Bussiness')
    def Work(self):
        print('I am Work For My Child')

class Father(GrandFather):
    def __init__(self,name):
        self.Health = 70
        self.Name = name
        self.Money = 200000

    def Work(self):
        print('I Am Work For Family')

class Son(Father):
    pass
obj1=Son('Sunit Kumar Gupta')
obj1.Intro()
obj1.Work()
print(obj1.Name,obj1.Money,obj1.Health)#Here We Can't Access Attributes of Grand-Father Class.'''
#But

class GrandFather:
    def __init__(self):
        self.health=70
        self.respect=100
        self.Money=300000

    def Intro(self):
        print('My Surname is Gupta')
        print('My Profession is Bussiness')
    def Work(self):
        print('I am Work For My Child')

class Father(GrandFather):
    def __init__(self,name):
        self.Health = 70
        self.Name = name
        self.Money = 200000

    def Work(self):
        print('I Am Work For Family')

class Son(Father):
    '''def __init__(self):
        GrandFather.__init__(self)'''
    def __init__(self,name):
        GrandFather.__init__(self)
        Father.__init__(self,name)
#obj1=Son()
#print('\n',obj1.respect,obj1.health)#Here We Can get The Attribute Data.
obj1=Son('Sunit Kumar Gupta')
print('\n',obj1.health,obj1.Name)