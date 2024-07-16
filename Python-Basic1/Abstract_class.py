#THIS PROGRAM IS HOW ABSTRACTION WORK AND HOW ABSTRACT CLASS IS CREATE AND WORK...
'''#CASE-1
#In Case-1 We See That Why Python Defaultly Not Take Empty Method As a Abstract Method...
from abc import ABC
class Vechile(ABC):
    def __init__(self,n):
        self.No_Of_Tyre=n
    def Start(self):
        pass
    def Display(self):
        print('I Am From Class Vechile(Abstract class)')
obj= Vechile(2)
'''
#CASE-2
#In Case-2 We See That How We Make a Method As Abstract...
from abc import ABC,abstractmethod
class Vechile(ABC):
    def __init__(self,n):
        self.No_Of_Tyre=n
    @abstractmethod#Destructor From Module abc
    def Start(self):
        pass
    def Display(self):
        print('I Am From Class Vechile(Abstract class)')
#obj= Vechile(2)#Now we could not make a obj of vechile(Because Now Vechile Is Abstract Class)
