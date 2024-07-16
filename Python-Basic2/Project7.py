#THIS PROGRAM IS SHOW HOW TO GUESS NO BETWEEN X TO Z....
import random,math,Logo
def Level():
    Cond=True
    while Cond:
        choice=input("Choose The Level OF Guessing(Hard/Easy):-")
        if choice.lower()=='hard':
            print("You Got 5 Attemps")
            return 5
        elif choice.lower()=='easy':
            print("You Got 10 Attemps")
            return 10
        else:
            print('Enter A valid Choice')
def Check(Data):
    Count=Level()
    while Count!=0:
        Input=int(input('Enter The NO:-'))
        if Data==Input:
            print("Your Guess No is Correct The No is ",Data)
            Count=0
        elif math.isclose(Input,Data,rel_tol=0.333333333)==True:
            print("You Are Too Close Please Try Again But Correct")
            Count=Count-1
        else:
            if Count==1:
                print("Your Loss All Attemps")
                print("Have a Good Day")
                Count = Count-1
            else:
                print("Your Guess Too Low")
                Count = Count-1
def Input():
    Data=random.randrange(1,50)
    print(Logo.Logo_For_Guess)
    print("Let Me Guess No From 1 To 50")
    Check(Data)
#Start
Input()












