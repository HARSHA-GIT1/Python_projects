#THIS PROGRAM IS SHOW HOW METHODS IS DECLARE AND INVOKE...
class Student:
    def __init__(self,Name,Age):#Here Self is a keyword which is used for passing obj.
        self.name=Name
        self.age=Age
#Intilizae a method.
    def Display(self,Carrer):
        print(f'Student Name is {self.name} and his age is {self.age} and he makes his career in {Carrer}')
        #There(Upper Statement) We Use Two Terms First Attribute(name And age) and Second is Parameter(Carrer)

#Simply Pass Data Differenty..
'''student1=Student("Harsh",19)
print(student1.name,student1.age)
student2=Student("Sunil",20)
print(student2.name,student2.age)
student3=Student("Abhimanyu",19)
print(student3.name,student3.age)'''

#OR
student1=Student("Neeraj",22)
student2=Student("Ganesh",21)
student3=Student("Raman",18)
student1.Display('Android Devloper')
student2.Display('Python')
student3.Display('Python')