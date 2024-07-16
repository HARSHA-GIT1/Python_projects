#THIS PROGRAM IS SHOWING HOW FUNCTION RETURN MULTI VALUE AND WORK WITH MULTI RETURN....
'''import statistics

def Mean_Meadian_Mode(list):
    return statistics.mean(list),statistics.median(list),statistics.mode(list)

List=[]
Data=0
size=int(input("Enter The Size Of List:"))
print("Enter The Element Of List:-")

for i in range(size):
    Data=int(input(""))
    List.append(Data)

print(Mean_Meadian_Mode(List))#Here Data Get in the form of Tuple..
result=list(Mean_Meadian_Mode(List))
print(result)
a,b,c=Mean_Meadian_Mode(List)
print(f'Mean is {a}\n Meadian is {b}\n Mode is {c}')'''

#Excercise for showing the working of multiple return value...
def Title(name):
    if name=="":
        return "Please Enter Name"
    else:
        name =name.title()
        return name
Name=input('Enter Your Name:- ')
result=Title(Name)
print("Result:",result)