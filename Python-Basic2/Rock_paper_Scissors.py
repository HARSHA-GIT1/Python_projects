#This Program Showing The Working of Rock,Paper and Scissors Game...
import random
print(f'0 For Rock \n1 for Paper \n2 For Scissors')
list=['Rock','Paper','Scissor']
userchoice= int(input('Enter Your Choice: '))
computerchoice= random.randint(0,2)
#This Trick Tell About The Result
if(0<=userchoice<3):
    if(userchoice==computerchoice):
        print("Draw")
        print(f'User Choice is {list[userchoice]}')
        print(f'Computer Choice is {list[computerchoice]}')
    elif(userchoice>computerchoice and userchoice !=2):
        print("User Won")
        print(f'User Choice is {list[userchoice]}')
        print(f'Computer Choice is {list[computerchoice]}')
    elif(computerchoice>userchoice and computerchoice!=2 ):
        print("Computer Won")
        print(f'User Choice is {list[userchoice]}')
        print(f'Computer Choice is {list[computerchoice]}')
    elif(computerchoice==2 and userchoice==0):
        print('User Won')
        print(f'User Choice is {list[userchoice]}')
        print(f'Computer Choice is {list[computerchoice]}')
    elif(computerchoice==0 and userchoice==2):
        print('Computer Won')
        print(f'User Choice is {list[userchoice]}')
        print(f'Computer Choice is {list[computerchoice]}')
else:
    print('Please Enter a Valid  Choice')
