#THIS PROGRAM IS SHOW HOW ABSTRACT_SUBCLASSES WORK...
from Abstract_class import *
class Bike(Vechile):
    def __init__(self,n,colour):
        self.No_Of_Tyre=n
        self.Colour=colour
    def Start(self):
        #print('Start With Kick')
        pass 
class Scooty(Vechile):
    def __init__(self,n):
        self.No_Of_Tyre=n
        self.Colour=colour
    def Start(self):
        print('Start With Kick and Self')
class Car(Vechile):
    def __init__(self,n,Type):
        self.No_Of_Tyre=n
        self.Type=Type
    def Start(self):
        print('Start With Self and By Human')