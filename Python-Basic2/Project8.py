#THIS PROGRAM IS SHOW HOW HIGHER VS LOWER GAME WORK...
import os
import Logo,random
#List For Names...
Data_Popul=[
          "PM Modi From Bharat",
          "MS Dhoni From Bharat",
          "Virat Kholi From Bharat",
          "Ronaldo From Portuguess",
          "Mukesh Ambani From Bharat",
          "Donald Trumph From USA",
          "Bill Gates From USA",
          "Mark Zurkerbug From USA",
          "Sundar Pichai From Google",
          "Ratan Ji Tata From Bharat",
          "Elon Mask From USA",
          "Isro From Bharat",
          "Messi From Argentine",
          "Instagram From Meta",
          "Google From Lengend Multi-Tech Companies",
          "Microsoft From Lengend Multi-Tech Companies",
          "IBM From Lengend Multi-Tech Companies",
          "Apple From Lengend Tech-Wears Companies",
          "Samsung From Lengend Tech-Wears Companies",
          "Netflix From Biggest OTT Plateform",
          "Mr Beast Biggest Youtubers",
          "T-Series Biggest Devotional-Music Company"
]
#List For Rank...
Data_Rank=[100,25,60,80,20,15,40,50,70,35,65,35,55,75,90,80,68,69,73,44,63,58]
def Condition(person1,rank1,count):
    Person2 = random.choice(Data_Popul)
    Rank2 = Data_Rank[Data_Popul.index(Person2)]
    print(person1,'Vs',Person2)
    print('Is',person1,"Rank Is High Or Not Compare To",Person2)
    condition=True
    while condition:
        Choice=input("Enter Your Choice(Higher/Lower):-")
        if Choice.lower()=='higher':
            if person1==Person2:
                continue

            elif rank1>Rank2:
                os.system('cls')
                print(Logo.Logo_For_Higher_Lower)
                count=count+1
                print('You Won Your Point Is:-',count)
                condition=False
                Condition(Person2,Rank2,count)#Recurrsion
            else:
                condition = False
                if count==0:
                    print('You Lose Your Point Is:-', count)
                else:
                    count=count-1
                    print('You Lose Your Point Is:-',count)
    #If User Enter Lower....
        elif Choice.lower()=='lower':
            if person1==Person2:
                continue

            elif rank1<Rank2:
                os.system('cls')
                print(Logo.Logo_For_Higher_Lower)
                count=count+1
                print('You Won Your Point Is:-',count)
                condition= False
                Condition(Person2,Rank2,count)#Recurrsion
            else:
                condition =False
                if count==0:
                    print('You Lose Your Point Is:-', count)
                else:
                    count=count-1
                    print('You Lose Your Point Is:-',count)
        else:
            print("Enter a Valid Choice")
def Start():
    #Getting Data Of First Popular Person Or Other...
    Person1=random.choice(Data_Popul)
    Rank1=Data_Rank[Data_Popul.index(Person1)]
    #Getting Data Of Second Popular Person Or Other...
    Count=0
    Condition(Person1,Rank1,Count)
#Start...
print(Logo.Logo_For_Higher_Lower)
Check=True
while Check:
    Start()
    choice=input("Do You Want To Play Again(Yes/No)")
    if choice.lower()=='yes':
        os.system('cls')
        print(Logo.Logo_For_Higher_Lower)
        Check=True
    elif choice.lower()=='no':
        Check=False
    else:
        print('Enter A valid Choice')
