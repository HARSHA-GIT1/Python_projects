#THIS PROGRAM IS SHOW HOW ACCESS SPECIFIERS WORKS...
#CASE-1(Public Specifer)
#NOTE:-
#(i). In Python Every Class And Attribute Deafaulty take public access specifer.
print('CASE-1(Public Specifer)')
class Student:
    def __init__(self,name,roll_no,age):
        self.Name=name
        self.Roll_No=roll_no
        self.Age=age
    def Display(self):
        print(f'Hii {self.Name} your age is {self.Age} and your roll no is {self.Roll_No}')
Student1=Student('Harsh Vardhan ',60,19)
Student1.Display()


#CASE-1(Protected Specifer)
print('\nCASE-1(Protected Specifer)')
#NOTE:-
#(i).In Python We have no features to restrict acessing the procteced data.
#(ii). This is Good Developer Responsibility to Give a proper access of protected attribute or method.
class Student:
    def __init__(self,name,roll_no,age):
        self.Name=name
        self._Roll_No=roll_no
        self.Age=age
    def _Display(self):
        print(f'Hii {self.Name} your age is {self.Age} and your roll no is {self._Roll_No}')
class Data(Student):
    pass
    def Show(self):
        print('Roll_No:-',self._Roll_No)
Student1=Data('Sunil Singh',75,21)
Student1._Display()
Student1.Show()
print(Student1._Roll_No)


#CASE-1(Private-Specifer)
print('\nCASE-1(Private Specifer)')
#NOTE:-
#(i).In Python We have also any features to restrict completly acessing the private  data.
#(ii). We have different way to acessing the private variable or method such as name magling using dir method in line 61.
class Student:
    def __init__(self,name,roll_no,age):
        self.Name=name
        self._Roll_No=roll_no
        self.__Age=age
    def Display(self):
        print(f'Hii {self.Name} your age is {self.__Age} and your roll no is {self._Roll_No}')
class Data(Student):
    pass
    def Show(self):
        print('Roll_No:-',self._Roll_No)
       #print('Age:-',self.__Age)
Student1=Data('Sunil Singh',75,21)
Student1.Display()
Student1.Show()
print(Student1._Roll_No)
#print(Student1.__Age)
print(dir(Student1))
print(Student1._Student__Age,'Here You can access private attribute out of the class using dir method in name magling')