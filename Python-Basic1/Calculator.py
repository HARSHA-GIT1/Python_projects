#THIS PROGRAM IS SHOWING THE WORKING OF CALCULATOR....
import os

List_of_Operation=['+','-','*','/','^','%']

#Function Is Showing The Working Of Calculation...
def Input(first):
    Condition = True
    result = 0
    while Condition:
        Choice=input("Enter The Operation:-")
        if Choice=='+':
            Second = int(input("Enter The Second No:-"))
            result=first+Second
            print(f'{first}+{Second}={result}')
            Condition=False
        elif Choice=='-':
            Second = int(input("Enter The Second No:-"))
            result=first-Second
            print(f'{first}-{Second}={result}')
            Condition = False
        elif Choice=='*':
            Second = int(input("Enter The Second No:-"))
            result=first*Second
            print(f'{first}*{Second}={result}')
            Condition = False
        elif Choice=='/':
            Second = int(input("Enter The Second No:-"))
            result=first/Second
            print(f'{first}/{Second}={result}')
            Condition = False
        elif Choice=='^':
            Second = int(input("Enter The Second No:-"))
            result=first^Second
            print(f'{first}^{Second}={result}')
            Condition = False
        elif Choice=='%':
            Second = int(input("Enter The Second No:-"))
            result=first%Second
            print(f'{first}%{Second}={result}')
            Condition = False
        else:
            print('Enter A Valid Choice')

    print("Press Y For Perform Another Operation With", result, "Or N For Perform New Operation Or X For Exit")
    condition=True

    while condition:
        choice=input("")
        if choice=='Y':
            os.system('cls')
            for i in List_of_Operation:
                print(i)
            Input(result)
            condition=False
        elif choice=='N':
            os.system('Cls')
            Enter()
            condition=False
        elif choice=='X':
            exit()
            condition=False
        else:
            print("Enter A Valid Choice(Enter Again)")

def Enter():
    First=int(input("Enter The First No:-"))
    for i in List_of_Operation:
        print(i)

    Input(First)

#Start
Enter()