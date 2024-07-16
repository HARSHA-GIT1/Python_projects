#THIS PROGRAM SHOW HOW ININT AND SELF WORK...
class Cars:
    def __init__(self,name,price):#This function is predefine function and it automatically call when object created..
        self.name=name
        self.price=price
        self.Model=0

obj1 = Cars("Maruti",2030000)
print(obj1.name,obj1.price)
#Defualt parameter..
class Cars:
    def __init__(self, name,price,Model=2023):
        self.name = name
        self.price = price
        self.Model = Model

obj1 = Cars("Maruti", 2030000)
print('Default Parameter')
print(obj1.name, obj1.price,obj1.Model)
#Defualt Attribute..
class Cars:
    def __init__(self,name,price):
        self.Name = name
        self.Price = price
        self.Model = 0

obj1 = Cars("Swift",4300000)
print('Default Attribute')
print(obj1.Name,obj1.Price,obj1.Model)