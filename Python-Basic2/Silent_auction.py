#This Program is Showing the Working of Silent-Auction...
#case 1:
''''import os
import math
Check=True
while Check:
    Name=input('Enter Your Name: ')
    Bid=int(input('Enter Your Bid: '))
    List_name=[]
    List_bid=[]
    List_name.append(Name)
    List_bid.append(Bid)
    Condition=input('Anyone Want For Bid: ')
    if Condition.lower()=='yes':
        os.system('cls')
        Check=True
    elif Condition.lower()=='no':
        Check=False
        Max=max(List_bid)
        print(List_name[List_bid.index(Max)],' is Won This Bid')
    else:
        print('Enter Valid Key ')'''
#case 2:
import os
def result(Dict_data):
    Max_Bid=0
    name=''
    for i in Dict_data:
        if Max_Bid < Dict_data[i]:
            Max_Bid = Dict_data[i]
            name=i
    print(f'{name} is Won this Bidding By Bid of {Max_Bid}')
Condition=True
while Condition:
    Name=input('Enter Your Name:')
    Bid=int(input('Enter Your Bid:'))
    Data={}
    Data[Name]=Bid
    Check=input('Anyone Want To Bid(Yes/No):')
    if Check.lower()=='yes':
        Condition = True
        os.system('cls')
    elif Check.lower()=='no':
        result(Data)
        Condition = False
