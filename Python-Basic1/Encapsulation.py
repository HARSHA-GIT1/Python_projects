#THIS PROGRAM IS BASICALLY SHOW HOW ENCAPSULATION WORK AND HOW TO GET PRIVATE DATA USIN GET AND SET METHOD.
class Student:
    def __init__(self,name,age):
        self.Name=name
        self.__Age=age
    def Display(self):
        print(f'Hello,{self.Name} How are you. I am just Ask  You are {self.__Age} year old')
#   {Here We Make a Get(For Getting Private Data) and Set(For Modified Private Data) Method.}
    def Get(self):#You Can use any name
        return self.__Age
    def Set(self,Age):
        self.__Age=Age

obj=Student('Harsh',19)
obj.Display()
#print(obj.__Age)
print('Age is :-',obj.Get())
obj.Set(21)
print('Now Age is:-',obj.Get())