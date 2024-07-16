#THIS PROGRAM IS SHOWING THE WORKING OF HANG-MAN GAME....
#First Case
'''print("Welcome To Hang Man Game")
print("You Have Only 6 Live for Win ...")
print("If You Enter Wrong Character Then One Live You Will Be Loss...")
import random
Presentdata=["Harsh",'Abhimanyu','Sunil',"Ganesh","Raman","Neeraj Da","Punit","Akshay"]
Predefine=str(random.choice(Presentdata))
List=[]
for i in range(len(Predefine)):
    List+="_"
print(List)
game_over=False
Life=6
while Life!=0:
    if('_' in List):
        data=input("Enter Your Choice: ")
        if data in List:
            print("You Have Entered It Already Please Enter A New Character:")
        else:
            if data in Predefine:
                print('Character is Match')
                Index=Predefine.index(data)
                List[Index]=data
                print(List)
            else:
                Life-=1
                print("Character is Not Match,You Lose a Life")
                print("You Have Left Only ",Life," Lifes Please Enter The Character After Thinking With Mind ")
    else:
        print('Congratulations You Won The Game ')
        print('Random Word is ',Predefine)
        break'''
#Second Case
print("Welcome To Hang Man Game")
print("You Have Only 6 Live for Win ...")
print("If You Enter Wrong Character Then One Live You Will Be Loss...")
import random
import hangman_Words
Predefine=str(random.choice(hangman_Words.Words))
List=[]
for i in range(len(Predefine)):
    List+="_"
print(List)
game_over=False
Life=6
while Life!=0:
    if('_' in List):
        data=input("Enter Your Choice: ")
        if data in List:
            print("You Have Entered It Already Please Enter A New Character:")
        else:
            if data in Predefine:
                print('Character is Match')
                Index=Predefine.index(data)
                List[Index]=data
                print(List)
            else:
                Life-=1
                if Life==0:
                    print("Character is Not Match")
                    print("Soory This is Your Last Chance ,You Lose The Game")
                    print("Words Is:",Predefine)
                else:
                    print("Character is Not Match,You Lose a Life")
                    print("You Have Left Only ",Life," Lifes Please Enter The Character After Thinking With Mind ")
    else:
        print('Congratulations You Won The Game ')
        print('Random Word is ',Predefine)
        break